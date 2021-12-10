from django.contrib import admin
from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path(
        "",
        views.InicioView.as_view()
        ,name="inicio"
        ),
    path(
        "listar-todo-empleados/", 
        views.ListAllempleados.as_view(),
        name="empleados_all"
        ),
    path(
        "listar-by-area/<shortname>/",
        views.ListByAreaEmpleado.as_view(),
        name="lista_depa"
        ),
    path("buscar-empleado/", views.ListEmpleadosByKword.as_view()),
    path("listar-habilidades-empleado/", views.Prueba.as_view()),
    path(
        "ver-empleado/<pk>/", 
        views.EmpleadoDetailView.as_view(),
        name="empleado_detail"
        ),
    path(
        "add-empleado/",
         views.EmpleadoCreateView.as_view(),
         name= "empleado_add"
         ),
    path("success/",views.SuccessView.as_view(),name="correcto"),
    path("update-empleado/<pk>/", views.EmpleadoUpdateView.as_view(),name="modificar_empleado"),
    path("delete-empleado/<pk>/",views.EmpleadoDeleteView.as_view(),name="eliminar_empleado"),
    path(
        "admin_empleados/", 
        views.ListaAdminempleados.as_view(),
        name="admin_all"
        ),
    
]