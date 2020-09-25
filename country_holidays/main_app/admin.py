from django.contrib import admin
from .models import Country
from .models import Holiday

# Register your models here.
admin.site.register(Country)
admin.site.register(Holiday)