from django import forms
from datetime import datetime
from apps.cliente.models.pessoa import Pessoa


class Leads(forms.ModelForm):
    data_criacao = forms.DateField(label='Data de Cadastro',disabled=True, initial=datetime.today)
    class Meta:
        model = Pessoa
        fields = '__all__'
        labels = {'nome':'Nome','cpf':'CPF','rg':'RG','Data_Nasc':'Data de Nascimento','telefone':'Telefone','email':'E-mail','cep':'CEP','logadouro':'Endereço','numero':'Número','bairro':'Bairro','complemento':'Complemento','uf':'UF','cidade':'Cidade','tipo_cliente':'Tipo'}
        data_criacao = forms.DateField(label='Data de Cadastro',disabled=True, initial=datetime.today)