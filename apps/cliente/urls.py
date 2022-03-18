from django.urls import path

from . import views

URLPatterns = [
    path('cadastro', views.cadastro, name='cadastro')
    
]