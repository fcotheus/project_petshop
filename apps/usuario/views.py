from django.shortcuts import render

def cadastro(request):
    return render(request,'usuario/cadastro_usuario.html')


def login(request):
    return render(request,'usuario/login.html')


