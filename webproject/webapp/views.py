from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("hai this is home page")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def details(request):
    return render(request,"details.html")

def thanks(request):
    return HttpResponse("thanks to all")

