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

class MadionDetailView(generic.DeleteView):
    model=models.Madion
    template_name = 'app/madion_detail.html'

#def index(request):
#    numebrOfmadion = models.Madion.objects.all().count()
#    numebrOfKarshenas = models.Karshenas.objects.all().count()
#    numebrOfModiriat = models.Modiriat.objects.all().count()
#    numebrOfShobe = models.Shobe.objects.all().count()


#    return render(
#        request,
#        'app/index.html',
#        context={'numebrOfmadion': numebrOfmadion,'numebrOfKarshenas': numebrOfKarshenas,'numebrOfModiriat': numebrOfModiriat,'numebrOfShobe': numebrOfShobe})
