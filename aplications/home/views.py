from aplications.home.models import Prueba
from django.shortcuts import render

# Create your views here.
from django.views.generic import *
from django.views.generic import(TemplateView, UpdateView, DeleteView ) 
from .models import Prueba
from .forms import PruebaForm

class PruebaView(TemplateView):
    template_name = "home/prueba.html"

class ResumeFoundationView(TemplateView):
    template_name = "home/resume_foundation.html"    



    
class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name ="listaNumeros"
    queryset = ["1","11","111","1111"]

class ListaPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model =Prueba
    context_object_name = "lista"

class PruebaCreateView(CreateView):
    template_name = "home/add.html"
    model = Prueba  
    form_class = PruebaForm
    success_url ="/"