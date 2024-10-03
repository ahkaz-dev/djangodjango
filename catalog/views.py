from django.http import HttpResponse
from django.template import loader

def cataloges(request):
  template = loader.get_template('catalog.html')
  return HttpResponse(template.render())