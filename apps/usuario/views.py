from re import match
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user != None:
            login(request, user)
            return redirect('/usuario/dashboard')

        messages.error(request, 'Usuário ou senha inválidos!')

    return render(request, 'usuario/login.html')

@login_required(login_url='/usuario/login')
def logout_usuario(request):
    logout(request)
    return redirect('/')





def cadastro_usuario(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if campo_vazio(username):
            messages.error(request,'O campo Usuario não pode ficar em branco')
            return redirect('/usuario/cadastro')
        if campo_vazio(email):
            messages.error(request,'O campo email não pode ficar em branco')
            return redirect('/usuario/cadastro')
        if User.objects.filter(email=email).count() > 0:
            messages.error(request, 'Este e-mail já foi cadastrado!')
            return redirect('/usuario/cadastro')

        if User.objects.filter(username=username).count() > 0:
            messages.error(request, 'Este usuário já foi utilizado!')
            return redirect('/usuario/cadastro')

        try:
            user = User.objects.create_user(first_name=name, username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
        except Exception:
            messages.error(request, 'Ocorreu algum erro ao cadastrar!')

        return redirect('/usuario/login')
    else:
        return render(request, 'usuario/cadastro_usuario.html')



        
def dashboard(request,rota = ''):
    if request.user.is_authenticated:
        print(rota)
        if rota == 'cadastro_servico':
            return render(request,'servicos/cadastro_servicos.html')
        elif rota == 'cadastro_cliente':
            return render(request, 'cliente/cadastro_pessoa.html' )
        elif rota == 'cadastro_pet':   
            return render(request, 'pet/cadastro_pet.html')
        else:    
            return render(request, 'usuario/dashboard.html')
    else:
        return redirect('/')

def campo_vazio(campo):
    return not campo.strip()
