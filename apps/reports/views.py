from typing import Generic
from django.http import request, response
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.views import View
from .forms import *
from apps.home.models import *
from apps.context_processors import *

class reports_view (TemplateView):
    template_name = 'reports/reports.html'


def filter_waste(initial, final):
    list = Sample.objects.filter(date__range(initial, final))
    return list


class area_waste_view (View):
    form_class = date_report_form
    template_name = 'reports/area_waste.html'

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
            contador = 0
            l_cont = []
            for k in courses:
                contador = 0
                for sample in list:
                    if k.name == sample.course: 
                        contador += 1
                l_cont.append(contador)
                obj = {
                    'program': k.program.name,
                    'area': k.program.area.name,
                    'cant': contador,                
                }
                result.append(obj)

            programs = Program.objects.filter(id__in = [i.id for i in courses])
            areas = courses.filter(id__in = [i.id for i in programs]) 


            programas = Program
            areas = list.count()

            # Waste Report per Course / Ficha
            # result = Sample.objects.filter(date__range=(initial, final))

        return render(request, self.template_name, locals())

