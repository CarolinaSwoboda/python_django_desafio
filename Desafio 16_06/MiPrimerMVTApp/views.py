from django.shortcuts import render

from django.http import HttpResponse

from django.template import Template,Context

import datetime

from MiPrimerMVTApp.models import *


# Create your views here.


def familia(request):
    
    personas = Familiare.objects.all()
    
    contexto = {"personas":personas}
        
    return render(request, r"MiPrimerMVTApp\index.html", contexto)

