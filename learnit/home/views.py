from django.shortcuts import render


def homepage(request):
    return render(request,'home/homepage.html')

def pricing(request):
    return render(request,'home/pricing.html')

def dashboard(request):
    return render(request,'home/dashboard.html')

def services(request):
    return render(request,'home/services.html')