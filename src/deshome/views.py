from django.shortcuts import render

def home_view(request):
    return render(request, "home.html", {})

def commerce_view(request):
    return render(request, "experimental.html", {})

def login_view(request):
    return render(request, "login.html", {})

def signin_view(request):
    return render(request, "signin.html", {})

