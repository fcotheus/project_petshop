from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('cliente/', include('cliente.urls')),
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),
    path('pet/', include('pet.urls')),
    path('servicos/', include('servicos.urls')),
    
]
