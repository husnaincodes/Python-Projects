
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "admin" and password == "123":
            request.session["user"] = username
            messages.success(request, "Login successful!")
            return redirect("Home")  # Go to homepage after login
        else:
            messages.error(request, "Wrong username or password!")

    return render(request, "login.html")

def logout_view(request):
    request.session.pop("user", None)
    messages.success(request, "You have been logged out!")
    return redirect("login")
