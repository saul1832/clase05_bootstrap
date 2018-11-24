from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listado(request):
    return render(request, "crud/listar.html")

def agregar(request):
    return render(request, "crud/agregar.html")