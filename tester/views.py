from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

def testing(request):
    context = {
        "delete": "Delete",
        "inner_content": "Are you sure you want to delete this?",
        "confirm_action": reverse("home"),
        "method": "post",
        "frag_confirm_maincolor": "#0a6912",
    }
    return render(request, "tester/index.html", context)

def home(request):
    return HttpResponse("This is home!!")
