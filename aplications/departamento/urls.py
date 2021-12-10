from django.contrib import admin
from django.urls import path
from . import views

def DesdeApps(self):
         print("hola mundo")

app_name = "departamento_app"         

urlpatterns = [
    
    path("new-departamento/", views.NewDepartamentoView.as_view(), name= "prueba_add"),
    path("lista-departamento/", views.DepartamentoListView.as_view(), name= "lista_departamento"),
]