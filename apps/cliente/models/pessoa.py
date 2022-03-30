from django.db import models


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
        ('TO','TO')
        )

    TIPO_CLIENTE = (
    ('ATIVO','Ativo'),
    ('INATIVO','Inativo'),
    ('PROSPECCAO','Prospecção'),
    )


    nome = models.CharField(max_length=200)
    cpf = models.IntegerField(max_length=200)
    rg = models.IntegerField(max_length=200,blank=True)
    data_nasc = models.DateField(blank=True)
    telefone = models.CharField(max_length=200)
    email = models.EmailField()
    cep= models.CharField(max_length=200,blank=True)
    logadouro = models.TextField(max_length=200,blank=True)
    numero = models.IntegerField(max_length=200,blank=True)
    bairro = models.CharField(max_length=200,blank=True)
    complemento = models.TextField(max_length=200,blank=True)
    uf = models.CharField(max_length=2,choices=UF_CHOICES,blank=True)
    cidade = models.TextField(max_length=200,blank=True)
    tipo_cliente = models.TextField(choices=TIPO_CLIENTE,max_length=15,default=0)
    data_cricao = models.DateField()