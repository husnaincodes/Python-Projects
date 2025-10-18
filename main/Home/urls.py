
from django.contrib import admin
from django.urls import path
from Home import views
admin.site.site_header = "Husnain Admin"
admin.site.site_title = "Husnain Admin Portal"
admin.site.index_title = "Welcome to husnaincodes愛 Portal"



urlpatterns = [
 path("",views.index,name="Home"),

 path("about",views.about,name="About"),
 path("project",views.project,name="Projects"),
 path("contact",views.contact,name="Contact")
]
