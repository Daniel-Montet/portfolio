from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

def index(request):
    return HttpResponse("Hello World")

def project(request):
    return render(request, 'polls:index')