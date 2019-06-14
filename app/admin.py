from django.contrib import admin
from . import models

#admin.site.register(models.Karshenas)


class ModiriatInline(admin.TabularInline):
    model = models.Shobe
    extra = 3


@admin.register(models.Karshenas)
class KarshenasAdmin(admin.ModelAdmin):
    fields=[('karshenas_id','karshenas_title')]

@admin.register(models.Madion)
class MadionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('اطلاعات مدیون' ,{'fields':('madion_id','madion_name','madion_compani')}),
        ('اطلاعات ضامن'  ,{'fields':('madion_zamen1','madion_zamen2','madion_zamen3')}),
        ('اطلاعات شعب'   ,{'fields':('shobe_name','modiriat_name')}),
        ('اطلاعات قرارداد',{'fields':('noe_madion','karshenas_name')}),
        ('اطلاعات اجرایی',{'fields':('kelase_asli','kelase_niabati')}),
        ('تاریخ ارجاع و عودت',{'fields':('date_erjae','odat_banck')}),

    )
    list_display = ('madion_name', 'karshenas_name','kelase_asli','kelase_niabati','date_erjae','noe_madion','modiriat_name')
    list_filter = ('madion_name', 'karshenas_name','kelase_asli','kelase_niabati','noe_madion','modiriat_name')

@admin.register(models.Shobe)
class ShobeAdmin(admin.ModelAdmin):
    fields=[('shobe_id','shobe_title','modiriat')]
    list_display = ('shobe_title', 'modiriat')
    list_filter = ('shobe_title', 'modiriat')


@admin.register(models.Modiriat)
class ModiriatAdmin(admin.ModelAdmin):
    fields=[('modiriat_id','modiriat_title')]
    inlines = [ModiriatInline]
