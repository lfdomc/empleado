from django import forms

class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField( max_length=50,)
    apellidos = forms.CharField( max_length=50,)
    departamento = forms.CharField( max_length=50,)
    shor_name = forms.CharField( max_length=50,)

