from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'cwApp/index.html')


def base(request):
    return render(request, 'cwApp/base.html')


def aboutpages(request):
    return render(request, 'cwApp/aboutpages.html')
