from django.shortcuts import render

def cadastro(request):
  return  render(request,'servicos/cadastro_servicos.html')