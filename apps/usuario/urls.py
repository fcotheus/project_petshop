from django.urls import path
from .import views

urlpatterns = [
    path('cadastro/', views.cadastro_usuario, name='cadastro-usuario'),
    path('login/', views.login_usuario, name='login-usuario'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/<rota>', views.dashboard, name='dashboard'),
]
