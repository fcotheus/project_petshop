from unicodedata import name
from django.urls import URLPattern, path

from . import views

URLPatterns = [
    path('', views.servicos, name='servicos')
]