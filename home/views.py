from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    return render(request, 'base.html')
def academics(request):
    return render(request, 'Academics.html')
def services(request):
    return render(request, 'Services.html')
def calendar(request):
    return render(request, 'Calendar.html')
def contact(request):
    return render(request, 'ContactUs.html')
def meet(request):
    return render(request, 'MeetTheTeam.html')