from django import forms
import datetime

class date_report_form (forms.Form):
    initial_date = forms.DateField(widget = forms.TextInput(attrs={'class':'form-control', 'type':'date'}), label='Fecha Inicial')
    final_date = forms.DateField(widget = forms.TextInput(attrs={'class':'form-control', 'type':'date'}), label='Fecha Final')

    # def clean_initial_date (self):
    #     initial_date = self.cleaned_data['initial_date']
    #     #final_date = self.cleaned_data['final_date']
        
    #     if initial_date > datetime.date.today():    
    #         raise forms.ValidationError('La fecha no puede ser superior a la fecha actual')
    #     # if final_date < initial_date:
    #     #     raise forms.ValidationError('Las fecha inicial debe ser menor o igual a la fecha final')
    #     else:
    #         return initial_date
    #     return super(date_report_form, self).clean()

    # def clean_final_date (self):
    #     initial_date = self.cleaned_data['initial_date']
    #     final_date = self.cleaned_data['final_date']
    #     print("xxxxxxxxxxxxxxxxx")
    #     print(initial_date)
    #     print(final_date)
    #     print("xxxxxxxxxxxxxxxxx")
    #     if final_date >= initial_date:
    #         pass
    #     elif final_date > datetime.date.today() or initial_date > datetime.date.today():
    #         raise forms.ValidationError('Las fecha final no puede ser superior a la fecha actual')
    #     else:
    #         raise forms.ValidationError('Las fecha final debe ser mayor o igual a la fecha final')
    #     return super(date_report_form, self).clean()
    

