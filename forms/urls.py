from django.contrib import admin
from django.urls import path
from form import views

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", views.home, name="Home"),
]
