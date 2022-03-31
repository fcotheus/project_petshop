from django import forms
from datetime import datetime
from tempus_dominus.widgets import DatePicker
from cliente.models import Pessoa


class LeadsForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
        labels = {'nome':'Nome','cpf':'CPF','rg':'RG','Data_Nasc':'Data de Nascimento','telefone':'Telefone','email':'E-mail','cep':'CEP','logadouro':'Endereço','numero':'Número','bairro':'Bairro','complemento':'Complemento','uf':'UF','cidade':'Cidade','tipo_cliente':'Tipo'}
        exclude = ['rg','data_nasc''cep','logadouro','numero','bairro','complemento','uf','cidade','tipo_cliente','data_criacao','cep']

class ClienteForms(forms.ModelForm):
    data_criacao = forms.DateField(label='Data de Cadastro',disabled=True, initial=datetime.today)
    class Meta:
        model = Pessoa
        fields = '__all__'
        labels = {'nome':'Nome','cpf':'CPF','rg':'RG','data_nasc':'Data de Nascimento','telefone':'Telefone','email':'E-mail','cep':'CEP','logadouro':'Endereço','numero':'Número','bairro':'Bairro','complemento':'Complemento','uf':'UF','cidade':'Cidade','tipo_cliente':'Tipo'}
        widgets = {
            'data_nasc':DatePicker()
        }
        data_criacao = forms.DateField(label='Data de Cadastro',disabled=True, initial=datetime.today)
        exclude = ['data_criacao']