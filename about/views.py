from django.shortcuts import render
from django.http import HttpResponse


def about_index(request):
    return render(request, 'about/about.html')
