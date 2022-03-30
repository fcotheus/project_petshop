from django.shortcuts import render
from cliente.forms import LeadsForms

def cadastro(request):
    return render(request, 'cliente/cadastro_pessoa.html')

def Lead(request):
    lead_form = LeadsForms()
    contexto = {'lead_form':lead_form}
    return render(request,'cliente/fale_conosco.html',contexto)    
