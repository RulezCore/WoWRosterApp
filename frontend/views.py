from django.shortcuts import render, HttpResponse, redirect
from api.models import Member, Raid


def home(request):
    if request.user.is_authenticated:
        return redirect('/raids')
    else:
        return render(request, "frontend/home.html")

def raids(request):
    return render(request, 'frontend/raids.html')

def members(request):
    members = Member.objects.all()
    return render(request, 'frontend/members.html', {'members': members})