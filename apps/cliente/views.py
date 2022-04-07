from ast import Try
from django.shortcuts import render, redirect
from apps.usuario.views import cadastro_usuario
from cliente.models  import Pessoa
from django.contrib import messages
from tempus_dominus.widgets import DatePicker
from datetime import datetime

def cadastro(request):
    if request.method == 'POST':
        name = request.POST['name']
        cpf = request.POST['cpf']
        rg = request.POST['rg']
        data_nasc = request.POST['data_nasc']
        telephone = request.POST['telephone']
        email = request.POST['email']
        cep = request.POST['cep']
        logadouro = request.POST['logadouro']
        numero = request.POST['numero']
        bairro = request.POST['bairro']
        complemento = request.POST['complemento']
        uf = request.POST['uf']
        tipo_cliente = request.POST['tipo_cliente']
        data_cricao = request.POST['data_cricao']

        try:
            cadastro_cliente = Pessoa()
            cadastro_cliente.name = name
            cadastro_cliente.cpf = cpf
            cadastro_cliente.rg = rg
            cadastro_cliente.data_nasc = data_nasc
            cadastro_cliente.telephone = telephone
            cadastro_cliente.email = email
            cadastro_cliente.cep = cep
            cadastro_cliente.logadouro = logadouro
            cadastro_cliente.numero = numero
            cadastro_cliente.bairro = bairro
            cadastro_cliente.complemento = complemento
            cadastro_cliente.uf = uf
            cadastro_cliente.tipo_cliente = tipo_cliente
            cadastro_cliente.data_cricao =  datetime.now()
            print(cadastro_cliente.data_cricao)
            cadastro_cliente.save()
            return redirect('dashboard')
        except Exception as error:
            print(error) 
            messages.error(request, 'Ocorreu algum erro enviar o formulário!')   
    return render(request, 'cliente/cadastro_pessoa.html' )

def Lead(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        telephone = request.POST['telephone']
        city = request.POST['city']
        cep = request.POST['cep']

        try:
            lead = Pessoa()
            lead.name = name
            lead.email = email
            lead.telephone = telephone
            lead.city = city
            lead.cep = cep
            lead.save()
            messages.success(request, 'Formulário enviado com sucesso!')
        except Exception as error:
            print(error)
            messages.error(request, 'Ocorreu algum erro enviar o formulário!')

        return redirect('/cliente/lead')
    
    return render(request, 'cliente/fale_conosco.html')    
  

