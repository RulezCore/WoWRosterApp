from django.shortcuts import render, HttpResponse
from api.models import Member


def home(request):
    members = Member.objects.all()
    return render(request, "frontend/home.html", {'members': members})
