from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def cataloges(request):
  return render(request, 'home.html')