from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'generator/home.html')

def gerador_view(request):
    return render(request, 'generator/gerador.html')

def suporte_view(request):
    return render(request, 'generator/suporte.html')