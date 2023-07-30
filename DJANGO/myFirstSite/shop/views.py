# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def page1(request):
    return HttpResponse("This is the home page of our shop")
