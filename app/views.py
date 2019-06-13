from django.shortcuts import render

from . import models

def index(request):
    numebrOfmadion = models.Madion.objects.all().count()
    numebrOfKarshenas = models.Karshenas.objects.all().count()
    numebrOfModiriat = models.Modiriat.objects.all().count()
    numebrOfShobe = models.Shobe.objects.all().count()


    return render(
        request,
        'app/index.html',
        context={'numebrOfmadion': numebrOfmadion,'numebrOfKarshenas': numebrOfKarshenas,'numebrOfModiriat': numebrOfModiriat,'numebrOfShobe': numebrOfShobe})
