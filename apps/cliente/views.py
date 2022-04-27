from pydoc import cli
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cliente.models import Pessoa
from tempus_dominus.widgets import DatePicker
from datetime import datetime


@login_required(login_url='/usuario/login')
def listar_clientes(request):
    clientes = Pessoa.objects.all()

    context = {
        'cliente': clientes
    }

    return render(request, 'cliente/listar_pessoa.html', context)


@login_required(login_url='/usuario/login')
def cadastro_cliente(request):
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
        city = request.POST['city']
        tipo_cliente = request.POST['tipo_cliente']

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
            cadastro_cliente.data_cricao = datetime.now().strftime("%d/%m/%Y")
            now = datetime.now()
            year = now.strftime("Y%")
            print('data',year)
            cadastro_cliente.save()
            # return redirect('dashboard')
        except Exception as error:
            print(error)
            messages.error(request, 'Ocorreu algum erro enviar o formulário!')
    return render(request, 'cliente/cadastro_pessoa.html')


@login_required(login_url='/usuario/login')
def editar_cliente(request, id):
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

        try:
            Pessoa.objects.filter(id=id).update(name=name, cpf=cpf, rg=rg, data_nasc=data_nasc, telephone=telephone, email=email,
                                  cep=cep, logadouro=logadouro, numero=numero, bairro=bairro, complemento=complemento, uf=uf, tipo_cliente=tipo_cliente)
            messages.success(request, 'Dados editados com sucesso!')
            return redirect('/cientes/listar')
        except Exception:
            messages.error(request, 'Ocorreu algum erro ao editar os dados!')

        return redirect('/cientes/listar')


@login_required(login_url='/usuario/login')
def apagar_cliente(request, id):
    try:   
        Pessoa.objects.filter(id=id).delete()
        messages.success(request, 'Dados apagados com sucesso!')
    except Exception:
        messages.error(request, 'Ocorreu algum erro ao apagar os dados!')

    return redirect('/cientes/listar')	

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
  

