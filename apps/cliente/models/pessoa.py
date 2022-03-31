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
        ('TO','TO'),
        )

    TIPO_CLIENTE = (
    ('ATIVO','Ativo'),
    ('INATIVO','Inativo'),
    ('PROSPECCAO','Prospecção'),
    )


    nome = models.CharField(max_length=100)
    cpf = models.IntegerField()
    rg = models.IntegerField(blank=True)
    data_nasc = models.DateField(blank=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    cep= models.CharField(max_length=15,blank=True)
    logadouro = models.CharField(max_length=100,blank=True)
    numero = models.IntegerField(blank=True)
    bairro = models.CharField(max_length=50,blank=True)
    complemento = models.CharField(max_length=50,blank=True)
    uf = models.TextField(choices=UF_CHOICES,max_length=2,default=0)
    cidade = models.CharField(max_length=200,blank=True)
    tipo_cliente = models.TextField(choices=TIPO_CLIENTE,max_length=15,default=0)
    # data_cricao = models.DateField()