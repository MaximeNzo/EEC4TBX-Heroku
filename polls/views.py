from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

# Create your views here.


def index(request):
    variable = "EEC4TBX Page"
    template = loader.get_template('polls/index.html')
    context = {
        'variable': variable,
        'STATIC_URL': "static/",
    }
    return HttpResponse(template.render(context,request))