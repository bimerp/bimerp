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