from typing import Generic
from django.http import request, response
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, FormView
from django.views import View
import json 
from .forms import *
from apps.home.models import *
from apps.context_processors import *

class reports_view (TemplateView):
    template_name = 'reports/reports.html'


def filter_waste(initial, final):
    list = Sample.objects.filter(date__range(initial, final))
    return list

class program_waste_view (View):
    form_class = date_report_form
    template_name = 'reports/program_waste.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            initial = form.cleaned_data['initial_date']
            final = form.cleaned_data['final_date']
            list = Sample.objects.filter(date__range=(initial, final))
            total = list.count()
            
            courses = Course.objects.filter(name__in = [i.course for i in list]) # fichas que hicieron esos reportes

            result = []
            program_counter = 0
            area_counter = 0
            l_cont = []

            lista = []
            aux = []

            for k in courses: # k is a Course/Ficha
                program_counter = 0
                for sample in list:
                    if k.name == sample.course:  #compare ficha/course name with sample course  
                        program_counter += 1 
                    # if k.program.area == sample.program.area:
                    #     area_counter += 1    
                l_cont.append(program_counter)
                obj = {
                    'program': k.program.name,
                    'area': k.program.area.name,
                    'cant': program_counter,                
                }
                result.append(obj)
                
                aux.append(k.program.name)
                aux.append(program_counter)
                lista.append(aux)
                aux = []


            cadena = json.dumps(lista)

            print("XXXXXXXXXXXX")
            print(area_counter)
            print("XXXXXXXXXXXX")

            programs = Program.objects.filter(id__in = [i.id for i in courses])
            areas = courses.filter(id__in = [i.id for i in programs]) 


            programas = Program
            areas = list.count()

            # Waste Report per Course / Ficha
            # result = Sample.objects.filter(date__range=(initial, final))

        return render(request, self.template_name, locals())


import openpyxl



class download_excel_view (View):
    form_class = date_report_form
    template_name = 'reports/download_excel.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            initial = form.cleaned_data['initial_date']
            final = form.cleaned_data['final_date']

            list = Sample.objects.filter(date__range=(initial, final))
            total = list.count()


            # create openpyxl workbook  and sheet   (sheet = excel sheet)
            wb = openpyxl.Workbook()
            sheet = wb.active
            sheet.title = "Reporte de Desviaciones"

            # create header 
            sheet['A1'] = 'Fecha del Registro'
            sheet['B1'] = 'Fecha de modificacion'
            sheet['C1'] = 'Volumen'
            sheet['D1'] = 'Instructor'
            sheet['E1'] = 'Ficha'
            sheet['F1'] = 'Programa'
            sheet['G1'] = 'Área'
            sheet['H1'] = 'Componentes'
            sheet['I1'] = 'Tipo'
            sheet['J1'] = 'Actividad u Origen'
            sheet['K1'] = 'Registrdo Por'

            # create data
            counter = 2
            for sample in list:
                sheet['A' + str(counter)] = str(sample.date_time)
                sheet['B' + str(counter)] = str(sample.date)
                sheet['C' + str(counter)] = sample.volume
                sheet['D' + str(counter)] = sample.instructor
                sheet['E' + str(counter)] = sample.course
                sheet['F' + str(counter)] = sample.course
                sheet['G' + str(counter)] = sample.course
                sheet['H' + str(counter)] = sample.components.name
                sheet['I' + str(counter)] = sample.components.type_name.name
                sheet['J' + str(counter)] = sample.origin.name
                sheet['K' + str(counter)] = sample.person.user.username
                counter += 1

            # save workbook
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=reporte.xlsx'
            wb.save(response)

            # return response to download
            #response = render(request, self.template_name, locals())

            return response            


            #courses = Course.objects.filter(name__in = [i.course for i in list]) # fichas que hicieron esos reportes


