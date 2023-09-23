from django.shortcuts import render

def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context)


def home(request):
    context = {}
    return render(request, 'home.html', context)