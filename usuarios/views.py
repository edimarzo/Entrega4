from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from usuarios.forms import FormularioRegistro, FormularioEdicionPerfil
from usuarios.models import InfoExtra

# Create your views here.
def login_usuario(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request,data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            clave = formulario.cleaned_data.get('password')
            
            usuario_autenticado = authenticate(username=usuario, password=clave)
            
            login(request, usuario_autenticado)
            InfoExtra.objects.get_or_create(user=usuario_autenticado)
            return redirect('inicio:inicio')
        else:
            return render(request,'usuarios/login.html',{'formulario':formulario})
    formulario = AuthenticationForm()      
    return render(request,'usuarios/login.html', {'formulario':formulario})





def registro(request):
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:login')
        else:
            return render(request,'usuarios/registro.html',{'formulario':formulario})
    formulario = FormularioRegistro()      
    return render(request,'usuarios/registro.html', {'formulario':formulario})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        formulario = FormularioEdicionPerfil(request.POST, request.FILES, instance=request.user)
            
        if formulario.is_valid():
            if formulario.cleaned_data.get('avatar'):
                request.user.infoextra.avatar = formulario.cleaned_data.get('avatar')
                request.user.infoextra.save()
            
            
            formulario.save()
            return redirect('usuarios:editar')
        else:
            return render(request,'usuarios/editar.html',{'formulario':formulario})
    formulario = FormularioEdicionPerfil(initial={'avatar':request.user.infoextra.avatar} , instance=request.user)      
    return render(request,'usuarios/editar.html', {'formulario':formulario})