from django.shortcuts import render, HttpResponse, redirect
from .models import Curso, Description
from django.contrib import messages

def index(request):
    temp=Curso.objects.all()
    context={
        'cursos': temp
    }
    return render(request, "index.html", context)
# Create your views here.
def agregar(request):
    error = Curso.objects.validacion(request.POST)
    if len(error) > 0:
        for key, value in error.items():
            messages.error(request, value)
        redirect("/")
    else:
        temp=Description.objects.create(descripcion=request.POST['form_desc'])
        Curso.objects.create(name=request.POST['nombre'], desc=temp)
    return redirect("/")

def confirmar_delete(request, op):
    print('imprimir')
    temp=Curso.objects.get(id=op)
    context = {
    'curso': temp
    }
    return render(request, "delete.html", context)

def eliminar(request, op):
    print("entro")
    temp=Curso.objects.get(id=int(op))
    temp.delete()
    return redirect("/")
