from django.db import models


class Servico(models.Model):
    SERVICO = (
    ('BANHO_TOSA','Banho e Tosa'),
    ('VETERINARIA','Veterinaria'),
    ('HIDRATACAO','Hidratação'),
    )
    PAGAMENTO = (
        ('DINHEIRO','Dinheiro'),
        ('DEBITO','Cartão de débito'),
        ('CREDITO','Cartão de crédito'),
        ('BOLETO','Boleto bancário'),
        ('PIX','Pix'))

    servico = models.TextField(choices=SERVICO,max_length=15,default=0)
    date_servico = models.DateField(blank=True)
    hora_servico = models.TimeField(blank=True,null=True)
    pagamento = models.CharField(choices=PAGAMENTO,max_length=40, default=0)
    # date_cricao = models.DateField(blank=True)