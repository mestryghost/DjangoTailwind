from django.shortcuts import render, redirect
from .models import User, Event, Submission

# Create your views here.

def home_page(request):
    users = User.objects.filter(party=True)
    events = Event.objects.all()
    context = {'users': users, 'event': events}
    return render(request, 'home.html', context)

def event_page(request):
    events = Event.objects.all()
    users = User.objects.filter(party=True)
    context = {'events' : events, 'users': users}
    return render(request, 'event.html', context)

def event_authenticate(request, pk):
    events = Event.objects.get(id=pk)
    context = {'events': events}

    if request.method == "POST":
        events.participants.add(request.user)
        return redirect('events', pk=events.id)

    return render(request, 'eventauth.html', context)

def login_page(request):
    users = User.objects.filter(party=True)
    context = {'users': users}
    return render(request, "login.html", context)

def signin_page(request):
    users = User.objects.filter(party=True)
    context = {'users': users}
    return render(request, "signin.html", context)

def aboutus_page(request):
    return render(request, "aboutus.html", {})
