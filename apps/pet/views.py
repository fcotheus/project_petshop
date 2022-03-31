from django.shortcuts import render
from pet.forms import PetForms

def cadastro(request):
   pet_form = PetForms()
   contexto = {'pet_form':pet_form}
   return render(request, 'pet/cadastro_pet.html',contexto)