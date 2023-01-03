from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'gclock.html')

def analytics(request):
    return render(request, 'nclock.html')

def about(request):
    return render(request, 'eclock.html')

def weather(request):
    return render(request, 'weather.html')