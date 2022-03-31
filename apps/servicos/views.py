from django.shortcuts import render
from servicos.forms import ServicoForms

def cadastro(request):
  servico_form = ServicoForms()
  contexto = {'servico_form':servico_form}
  return  render(request,'servicos/cadastro_servicos.html',contexto)