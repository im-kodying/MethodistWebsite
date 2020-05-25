from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name = 'homepage'),
    path('academics/', academics, name = 'academics'),
    path('services/', services, name = 'services'),
    path('calendar/', calendar, name = 'calendar'),
    path('contact/', contact, name = 'contact'),
    path('meet/', meet, name = 'meet'),
    path('donate/', meet, name = 'donate'),
]