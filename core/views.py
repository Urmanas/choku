from django.shortcuts import render

from tours.models import Tour

def index(request):
    return render(request, 'core/index.html')

def home(request):
    tours = Tour.objects.all()
    return render(request, 'core/home.html', {
        'tours': tours
    })