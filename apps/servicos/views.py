from pydoc import cli
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from servicos.models import Servico

@login_required(login_url='/usuario/login')
def listar_servicos(request):
	servicos = Servico.objects.all()

	context = {
		'servicos': servicos
	}

	return render(request, 'servicos/listar_servicos.html', context)

@login_required(login_url='/usuario/login')
def cadastro_servicos(request):
	if request.method == 'POST':
		client = request.POST['client']
		animal = request.POST['animal']
		type = request.POST['type']
		payment = request.POST['payment']

		try:
			servico = Servico()
			servico.client = client
			servico.animal = animal
			servico.type = type
			servico.payment = payment
			servico.save()
			messages.success(request, 'Cadastro realizado com sucesso!')
		except Exception:
			messages.error(request, 'Ocorreu algum erro ao cadastrar!')

		return redirect('/servicos/cadastro')

	return render(request, 'servicos/cadastro_servicos.html')

@login_required(login_url='/usuario/login')
def editar_servico(request, id):
	if request.method == 'POST':
		client = request.POST['client']
		animal = request.POST['animal']
		type = request.POST['type']
		payment = request.POST['payment']

		try:
			Servico.objects.filter(id=id).update(client=client, animal=animal, type=type, payment=payment)
			messages.success(request, 'Dados editados com sucesso!')
			return redirect('/servicos/listar')
		except Exception:
			messages.error(request, 'Ocorreu algum erro ao editar os dados!')

		return redirect('/servicos/listar')

	servico = Servico.objects.filter(id=id)[0]

	context = {
		'servico': servico
	}

	return render(request, 'servicos/editar_servico.html', context)

@login_required(login_url='/usuario/login')
def apagar_servico(request, id):
	try:
		Servico.objects.filter(id=id).delete()
		messages.success(request, 'Dados apagados com sucesso!')
	except Exception:
		messages.error(request, 'Ocorreu algum erro ao apagar os dados!')

	return redirect('/servicos/listar')
