from django.shortcuts import render
from django.contrib import auth, messages

def index(request):
    return render(request,'home/index.html')

