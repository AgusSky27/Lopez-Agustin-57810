from django.contrib import admin

# Register your models here.
from .models import *

class CostaAdmin(admin.ModelAdmin):
    list_display = ("apellido","nombre", "cabaña")

class NaturAdmin(admin.ModelAdmin):
    list_display = ("apellido","nombre", "cabaña")

class RayenAdmin(admin.ModelAdmin):
    list_display = ("apellido","nombre", "cabaña")

admin.site.register(Costa, CostaAdmin)
admin.site.register(Natur, NaturAdmin)
admin.site.register(Rayen, RayenAdmin)
