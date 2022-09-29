from django.contrib import admin  
from .models import resources,login,status
from mapbox_location_field.admin import MapAdmin  
  
admin.site.register(resources, MapAdmin)  
admin.site.register(login)
admin.site.register(status)
# Register your models here.
