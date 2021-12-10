from typing import List
from django.shortcuts import render
from django.views.generic import *
from django.views.generic import(TemplateView, UpdateView, DeleteView ) 


from django.urls import reverse_lazy
from .models import Empleado
# Create your views here.


class InicioView(TemplateView):
    #vista que carga la pagina de Inicio#
    template_name = "inicio.html"


class ListAllempleados(ListView):
    
    template_name = 'persona/list_all.html'
    paginate_by = 5
    ##ordering = ['id','last_name']
    context_object_name ="empleados"

    def get_queryset(self):
        print("********--------*******")
        palabra_clave = self.request.GET.get("kword","")
        lista = Empleado.objects.filter(
        first_name__icontains= palabra_clave
        )
        lista = Empleado.objects.order_by('id')
        print(lista)
        return lista

class ListByAreaEmpleado(ListView):
        ## Lista de empleados de un area ##
    template_name = 'persona/list_by_area.html'

    def get_queryset(self):
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
        departamento__name = area
        )
        return lista

class ListEmpleadosByKword(ListView):

    ## lista empleados por palabra ##
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('***************')
        palabra_clave = self.request.GET.get("kword","")

        lista = Empleado.objects.filter(
        first_name = palabra_clave
        )
        return lista

class ListaHabilidades(TemplateView):

    template_name = 'persona/habilidades.html'
    paginate_by = 4
    ordering = "first_name"
    model = Empleado
    
    
class Prueba(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = "habilidades"

    def get_queryset(self) :
        empleado = Empleado.objects.get(id=2)
        print(empleado.habilidades.all())
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context["titulo"]= " Empleado del mes"
        return context


class SuccessView(TemplateView):
    template_name = "persona/success.html"

 
class EmpleadoCreateView(CreateView):
     model = Empleado
     template_name = "persona/add.html"
     fields =[
         "first_name",
         "last_name",
         "job",
         "departamento",
         "habilidades",
         "avatar",
         ]
     #fields = ("__all__")
     success_url = reverse_lazy('persona_app:correcto')

     def  form_valid(self,form):

         empleado =form.save()
         empleado.full_name = empleado.first_name + ' '+ empleado.last_name
         empleado.save()

         return super(EmpleadoCreateView,self).form_valid(form)



class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields =[
         "first_name",
         "last_name",
         "job",
         "departamento",
         "habilidades",
         ]
    success_url = reverse_lazy('persona_app:admin_all')
    
    def post(self, request, *args, **kwargs):
       self.object = self.get_object()
       print("***********************************")
       print(request.POST)
       print(request.POST["last_name"])
       print("***********************************")




       return super().post(request, *args, **kwargs)     

    def  form_valid(self,form):

         print("++++++++++++++++++++++++++++++++++++")

         return super(EmpleadoUpdateView,self).form_valid(form)   


 
class EmpleadoDeleteView(DeleteView):
     model = Empleado
     template_name = "persona/delete.html"
     success_url = reverse_lazy('persona_app:admin_all')     



class ListaAdminempleados(ListView):
    template_name = 'persona/admin_empleado.html'
    paginate_by = 10
    ordering = "last_name"
    context_object_name ="empleados"

    def get_queryset(self):
        print("********--------*******")  
        palabra_clave = self.request.GET.get("kword","")
        lista = Empleado.objects.filter(
        first_name__icontains= palabra_clave
        )
        lista = Empleado.objects.order_by('id')
        print(lista)
        return lista