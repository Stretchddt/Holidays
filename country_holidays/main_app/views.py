import requests
import os
from django.shortcuts import render
from .forms import SearchCountry
from .models import Country
from .models import Holiday
from .forms import SearchHolidays

# Create your views here.
def home(request):
    return render(request, 'main_app/home.html')

def holiday_search(request):

    if request.method == 'POST':
        form = SearchCountry(request.POST or None)
        if form.is_valid():
            country = form.cleaned_data['country']
            year = form.cleaned_data['year']

            country_count = Country.objects.filter(country=country).count()
            if country_count == 0:
                BASE_URL = 'https://calendarific.com/api/v2'
                HOLIDAY_ENDPOINT = '/holidays'
                API_KEY = os.environ.get('CAL_API_KEY')
                COUNTRY = country
                YEAR = year
                FULL_URL = f'{BASE_URL}{HOLIDAY_ENDPOINT}?&api_key={API_KEY}&country={COUNTRY}&year={YEAR}'

                response = requests.get(FULL_URL)
                holidays = response.json()

                form.save()
                # Save to Country model
                country_details = {
                    'country': holidays['response']['holidays'][0]['country']['name'],
                    'year': holidays['response']['holidays'][0]['date']['iso']
                }

                # Save to Holidays model
                h = holidays['response']['holidays']
                len_h = len(h)
                for i in range(len_h):
                    holiday = h[i]['name']
                    description = h[i]['description']
                    date = h[i]['date']['iso']
                    location = h[i]['locations']
                    states = h[i]['states']
                    _type = h[i]['type']
                    current = Holiday(holiday=holiday, description=description, date=date, location=location, states=states, _type=_type, country=Country.objects.get(country=COUNTRY))
                    current.save()

            else:
                pass


    else:
        form = SearchCountry()


    context = {
        'form': form,
    }
    return render(request, 'main_app/search.html', context)

def display_holidays(request):

    holidays = ''
    country = ''
    if request.method == 'POST':
        form = SearchHolidays(request.POST or None)
        if form.is_valid():
            country = form.cleaned_data['country']
            holidays = Country.objects.get(country=country).holiday_set.all()
    else:
        form = SearchHolidays()

    context = {
        'form': form,
        'country': country,
        'holidays': holidays
    }
    return render(request, 'main_app/details.html', context)