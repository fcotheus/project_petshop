from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_clientes, name='listar-clientes'),
    path('cadastro/', views.cadastro_cliente, name='cadastro-cliente'),
    path('editar/<int:id>', views.editar_cliente, name='editar-cliente'),
    path('apagar/<int:id>', views.apagar_cliente, name='apagar-cliente'),
    path('lead',views.Lead, name='lead')
    
]