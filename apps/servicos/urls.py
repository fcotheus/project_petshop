from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_servicos, name='listar-servicos'),
    path('cadastro/', views.cadastro_servicos, name='cadastro-servicos'),
    path('editar/<int:id>', views.editar_servico, name='editar-servico'),
    path('apagar/<int:id>', views.apagar_servico, name='apagar-servico'),
]
