from django.forms import ModelForm 
from .models import Country

class SearchCountry(ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

class SearchHolidays(ModelForm):
    class Meta:
        model = Country
        fields = ['country']