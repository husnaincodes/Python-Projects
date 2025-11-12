from django.shortcuts import render,HttpResponse
from Home.models import Contact
from datetime import datetime

def index(request):
    return render(request,"project1.html")
    # return HttpResponse("This is Home page")

def about(request):
    # return HttpResponse("This is About page")
    return render(request,"about.html")
def project(request):
    # return HttpResponse("This is Projects  page")
    return render(request,"projects.html")
def contact(request):
    # return HttpResponse("This is Contact page")
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact = Contact(name=name,email=email,message=message,date= datetime.today())
        contact.save()
    return render(request,"contact.html")