from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.holiday_search, name='search'),
    path('details/', views.display_holidays, name='details'),
]