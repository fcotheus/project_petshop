from django.db import models

class Servico(models.Model):
    client = models.CharField(max_length=50, blank=True, default='')
    animal = models.CharField(max_length=50, blank=True, default='')

    TYPES = (
        ('banho', 'Banho'),
        ('tosa', 'Tosa'),
        ('vacina', 'Vacina')
    )

    PAYMENTS = (
        ('money', 'Dinheiro'),
        ('card', 'Cartão de crédito'),
        ('bank-transfer', 'Transferência bancária'),
        ('pix', 'Pix')
    )

    type = models.CharField(max_length=6, blank=True, choices=TYPES, default='')
    payment = models.CharField(max_length=50, blank=True, choices=PAYMENTS, default='')

    def __str__(self):
        return str(self.type)
