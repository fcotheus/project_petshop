from django.urls import path

from . import views

urlpatterns = [
    path('listar/', views.listar_pets, name='listar-pets'),
    path('cadastro/', views.cadastro_pet, name='cadastro-pet'),
    path('editar/<int:id>', views.editar_pet, name='editar-pet'),
    path('apagar/<int:id>', views.apagar_pet, name='apagar-pet'),
]