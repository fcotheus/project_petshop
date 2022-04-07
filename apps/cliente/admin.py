from django.contrib import admin
from cliente.models import Pessoa

@admin.register(Pessoa)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
