from django.shortcuts import render,HttpResponse,redirect

def index(request):
    if "user" not in request.session:
        return redirect("login")   # redirects to login page
    return render(request, "project1.html")

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