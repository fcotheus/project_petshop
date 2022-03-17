from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    # path('usuario/', include('usuario.urls')),
    # path('pet/', include('pet.urls')),
    # path('cliente/', include('cliente.urls')),
    # path('servicos/', include('servicos.urls')),
    
]
