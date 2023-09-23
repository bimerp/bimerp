from django.shortcuts import render

def admin(request):
    context = {}
    return render(request, 'admin.html', context)


def home(request):
    context = {}
    return render(request, 'home.html', context)



def login(request):
    context = {}
    return render(request, 'login.html', context)


def register(request):
    context = {}
    return render(request, 'register.html', context)