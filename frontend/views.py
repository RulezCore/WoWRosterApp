from django.shortcuts import render, HttpResponse
from api.models import Member, Raid


def home(request):
    raids = Raid.objects.all()
    return render(request, "frontend/home.html", {'raids': raids})
