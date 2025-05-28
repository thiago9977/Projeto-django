from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse(render(request, 'recipes/pages/home.html',context={'name': 'Bolo'}))

def recipes(request, id):
    return HttpResponse(render(request, 'recipes/pages/home.html',context={'name': 'Bolo'}))

