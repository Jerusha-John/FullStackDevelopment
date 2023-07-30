from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def home(request):
    # return HttpResponse("Hello World")
    products = Product.objects.all()
    return render(request,'index.html',{'products':products}) 

def contact(request):
    return HttpResponse("This is the contact page")

def about(request):
    return HttpResponse("This is the about page")        


       