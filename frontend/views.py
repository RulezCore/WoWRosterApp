from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import AuthenticationForm
from api.models import Member, Raid


def home(request):
    if request.user.is_authenticated:
        return redirect('/raids')
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')
    return render(request, "frontend/home.html", {'form':form})

def raids(request):
    raids = Raid.objects.all()
    return render(request, 'frontend/raids.html', {'raids':raids})

def raid(request, id):
    raid = Raid.objects.get(pk=id)
    return render(request, 'frontend/raid.html', {'raid':raid})

def members(request):
    members = Member.objects.all()
    return render(request, 'frontend/members.html', {'members': members})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')