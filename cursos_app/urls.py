from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.agregar),
    path('eliminar_confirm/<op>', views.confirmar_delete),
    path('delete/<op>', views.eliminar),
    path('delete_ajax/<op>', views.eliminar_ajax)
]
