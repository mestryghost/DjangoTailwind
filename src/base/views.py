from django.shortcuts import render
from .models import User, Event, Submission

# Create your views here.

def home_page(request):
    users = User.objects.filter(party=True)
    events = Event.objects.all()
    context = {'users', users}
    return render(request, 'home.html', context)

def event_page(request, pk):
    event = Event.obects.get(id=pk)
    context = {'event' : event}
    return render(request, 'event.html', context)