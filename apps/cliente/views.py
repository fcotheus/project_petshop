from django.shortcuts import render
from cliente.forms import LeadsForms, ClienteForms

def cadastro(request):
    cliente_form = ClienteForms()
    contexto = {'cliente_form':cliente_form}
    return render(request, 'cliente/cadastro_pessoa.html',contexto)

def Lead(request):
    lead_form = LeadsForms()
    contexto = {'lead_form':lead_form}
    return render(request,'cliente/fale_conosco.html',contexto)    
