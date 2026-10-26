from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def myfunction(request):
    return HttpResponse("introduction to django..!")
def about_view(request):
    return HttpResponse("welcome to django..!")