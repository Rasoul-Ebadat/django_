from django.db import models
import uuid
from django.urls import reverse


class Madion(models.Model):
    madion_id=models.UUIDField(primary_key = True,default=uuid.uuid4,help_text = 'Unique Id for this particular Madion' )
    madion_name = models.CharField(max_length = 100)
    madion_compani =models.CharField(max_length = 100)
    madion_zamen1 = models.CharField(max_length = 100)
    madion_zamen2 = models.CharField(max_length = 100)
    madion_zamen3 = models.CharField(max_length = 100)

    noe_madion = (
        ('R','رهنی'),
        ('Z','لازم الاجرا'))

    modiriat_name = models.ForeignKey('Modiriat',on_delete=models.SET_NULL,null=True)
    shobe_name    = models.ForeignKey('Shobe',on_delete=models.SET_NULL,null=True)
    karshenas_name = models.ForeignKey('Karshenas',on_delete=models.SET_NULL,null=True)
    date_erjae = models.DateField(null=True,blank=True)
    kelase_asli= models.CharField(max_length = 100)
    kelase_niabati= models.CharField(max_length = 100)
    odat_banck = models.DateField(null=True,blank=True)


    def __str__(self):
        return '%s,%s'%(self.madion_name)



class Shobe (models.Model):

    shobe_id = models.UUIDField(primary_key = True,default=uuid.uuid4,help_text = 'Unique Id for this particular Shobe' )
    shobe_title=models.CharField(max_length=200)
    modiriat = models.ForeignKey('Modiriat',on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return '%s,%s'%(self.shobe_title)


class Karshenas (models.Model):
      karshenas_title=models.CharField(max_length=200)
      karshenas_id  =models.UUIDField(primary_key = True,default=uuid.uuid4,help_text = 'Unique Id for this particular Karshenas' )
      def __str__(self):
         return '%s,%s'%(self.karshenas_title)



class Modiriat (models.Model):
      modiriat_title=models.CharField(max_length=200)
      modiriat_id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Unique Id for this particular Modiriat')

      def __str__(self):
         return '%s,%s'%(self.modiriat_title)
