from django.shortcuts import render,HttpResponse

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
    return render(request,"contact.html")