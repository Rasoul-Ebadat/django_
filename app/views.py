from django.shortcuts import render
from django.views import generic
from . import models


class Index(generic.TemplateView):

    template_name = 'app/index.html'

    def get_context_data(self,**Kwargs):
        context = super().get_context_data(**Kwargs)
        context['numebrOfmadion']= models.Madion.objects.all().count()
        context['numebrOfKarshenas']= models.Karshenas.objects.all().count()
        context['numebrOfModiriat']= models.Modiriat.objects.all().count()
        context['numebrOfShobe']= models.Shobe.objects.all().count()
        return context

class MadionListView(generic.ListView):
    model = models.Madion
    template_name = 'app/madion_list.html'

class MadionDetailView(generic.DetailView):
    model=models.Madion
    template_name = 'app/madion_detail.html'

class KarshenasListView(generic.ListView):
    model = models.Karshenas
    template_name = 'app/karshenas_list.html'

class KarshenasDetailView(generic.DetailView):
    model=models.Karshenas
    template_name = 'app/karshenas_detail.html'



class ShobeListView(generic.ListView):
    model = models.Shobe
    template_name = 'app/shobe_list.html'

class ShobeDetailView(generic.DetailView):
    model=models.Shobe
    template_name = 'app/shobe_detail.html'



class ModiriatListView(generic.ListView):
    model = models.Modiriat
    template_name = 'app/modiriat_list.html'

class ModiriatDetailView(generic.DetailView):
    model=models.Modiriat
    template_name = 'app/modiriat_detail.html'
