from django.shortcuts import render

def cadastro(request):
   return render(request, 'pet/cadastro_pet.html')