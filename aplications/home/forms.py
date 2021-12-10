from django import forms
from django.forms import widgets
from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        model = Prueba
        fields = ("titulo",
                  "subtitulo",
                  "cantidad",
        )
        widgets ={
                "cantidad" : forms.TextInput(
                       attrs= {
                           "placeholder" : "Ingrese texto aquí",
                           "color": "red"



                       }


                )



        }



    def clean_cantidad(self):
            cantidad = self.cleaned_data['cantidad']
            if cantidad <10 :
                raise forms.ValidationError("**El valos es menor a 10**" )
        
            return cantidad         
