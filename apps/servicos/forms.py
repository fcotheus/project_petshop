from django import forms
from datetime import datetime
from tempus_dominus.widgets import DatePicker
from servicos.models import Servico


class ServicoForms(forms.ModelForm):
    date_criacao = forms.DateField(label='Data de Cadastro',disabled=True, initial=datetime.today)       
    class Meta:
        model = Servico
        fields = '__all__'
        # labels = {}
        widgets = {
            'nasc':DatePicker()
        }
        exclude = ['date_criacao']
