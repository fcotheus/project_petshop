from django.shortcuts import render
from django.contrib import auth, messages

def index(request):
    messages.error(request,'O campo nome não pode ficar em branco')
    return render(request,'home/index.html')