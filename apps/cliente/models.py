from django.db import models
from statistics import mode

class Pessoa(models.Model):
    UF_CHOICES = (
        ('AC','AC'),
        ('AL','AL'),
        ('AP','AP'),
        ('AM','AM'),
        ('BA','BA'),
        ('CE','CE'),
        ('DF','DF'),
        ('ES','ES'),
        ('GO','GO'),
        ('MA','MA'),
        ('MT','MT'),
        ('MS','MS'),
        ('MG','MG'),
        ('PA','PA'),
        ('PB','PB'),
        ('PR','PR'),
        ('PE','PE'),
        ('PI','PI'),
        ('RJ','RJ'),
        ('RN','RN'),
        ('RS','RS'),
        ('RO','RO'),
        ('RR','RR'),
        ('SC','SC'),
        ('SP','SP'),
        ('SE','SE'),
        ('TO','TO'),
        )

    TIPO_CLIENTE = (
    ('ATIVO','Ativo'),
    ('INATIVO','Inativo'),
    ('PROSPECCAO','Prospecção'),
    )


    name = models.CharField(max_length=100, default='')
    cpf = models.CharField(max_length=20, blank=True)
    rg = models.CharField(max_length=20, blank=True, default='')
    data_nasc = models.DateField(blank=True)
    telephone = models.CharField(max_length=20, default='')
    email = models.EmailField()
    cep= models.CharField(max_length=15,blank=True, default='')
    logadouro = models.CharField(max_length=100,blank=True, default='')
    numero = models.CharField(max_length=20, blank=True, default='')
    bairro = models.CharField(max_length=50,blank=True, default='')
    complemento = models.CharField(max_length=50,blank=True, default='')
    uf = models.TextField(choices=UF_CHOICES,max_length=2, default=0)
    city = models.CharField(max_length=200,blank=True,default='')
    tipo_cliente = models.TextField(choices=TIPO_CLIENTE,max_length=15, default=0)
    data_cricao = models.DateField()

    def __str__(self):
        return str(self.name)