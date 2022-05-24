# Generated by Django 4.0.3 on 2022-03-31 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(blank=True, default='', max_length=50)),
                ('animal', models.CharField(blank=True, default='', max_length=50)),
                ('type', models.CharField(blank=True, choices=[('banho', 'Banho'), ('tosa', 'Tosa'), ('vacina', 'Vacina')], default='', max_length=6)),
                ('payment', models.CharField(blank=True, choices=[('money', 'Dinheiro'), ('card', 'Cartão de crédito'), ('bank-transfer', 'Transferência bancária'), ('pix', 'Pix')], default='', max_length=50)),
            ],
        ),
    ]
