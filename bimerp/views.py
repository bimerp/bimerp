from django.shortcuts import render

def backend(request):
    context = {}
    return render(request, 'backend_base.html', context)