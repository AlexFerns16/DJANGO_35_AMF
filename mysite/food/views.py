from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1 style="color:crimson">This is an index view</h1>')

def detail(request):
    return HttpResponse('<h1 style="color:blue">This is a detail view</h1>')
