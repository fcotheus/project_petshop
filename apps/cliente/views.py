from django.shortcuts import render

def cadastro(request):
    return render(request, 'cliente/cadastro_pessoa.html')
