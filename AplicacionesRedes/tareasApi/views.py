from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'tareasApi/index.html')

def tareas(request):
    return render(request, 'tareasApi/tareas.html')