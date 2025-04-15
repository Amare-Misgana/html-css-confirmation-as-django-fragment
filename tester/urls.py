from django.urls import path
from . import views

urlpatterns = [
    path("", views.testing, name="tester_url"),
    path("home/", views.home, name="home"),
]
