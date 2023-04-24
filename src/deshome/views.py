from django.shortcuts import render

def home_view(request):
    return render(request, "pages/home.html", {})

def commerce_view(request):
    return render(request, "pages/index.html", {})
