from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse("Hola k ase")
