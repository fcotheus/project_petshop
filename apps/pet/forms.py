from django import forms
from datetime import datetime
from tempus_dominus.widgets import DatePicker
from pet.models import Pet


class PetForms(forms.ModelForm):
    date_criacao = forms.DateField(label='Data de Cadastro',disabled=True, initial=datetime.today)       
    class Meta:
        model = Pet
        fields = '__all__'
        labels = {'nome':'Nome','nasc':'Nascimento','especie':'Espécie','raca':'Raça','cor':'Cor','idade':'Idade','porte':'Porte','sexo':'Sexo','date_cricao':'Data de Cadastro'}
        widgets = {
            'nasc':DatePicker()
        }
        sexo = forms.ChoiceField(
            label= 'Sexo',
            choices=[('M','Macho'),('F','Fêmea')],
            initial= 'M',
            widget = forms.RadioSelect,
        )
        # date_criacao = forms.DateField(label='Data de Cadastro',disabled=True, initial=datetime.today)
        exclude = ['date_criacao']
