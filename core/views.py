from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def carreras(request):
    lista_carreras = ["Ingenieria Civil Informatica", "Ingenieria em Informatica", "Ingenieria en Ejecucion de Software",]
    return render(request, 'core/carreras.html', {'carreras': lista_carreras})

def docentes(request):
    lista_docentes = ["Pamela Gatica", "Docente 2", "Docente 3",]
    return render(request, 'core/docentes.html', {'docentes' : lista_docentes})


