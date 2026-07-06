from django.conf import settings
from django.db import models
from apps.finances.enums import FormaPagamento

class Despesa(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='despesas',
    )

    categoria = models.ForeignKey(
        'finances.Categoria',
        on_delete=models.PROTECT,
        related_name='despesas',
    )

    descricao = models.CharField(max_length=150)

    valor = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    data = models.DateField()

    forma_pagamento = models.CharField(
        max_length=30,
        choices=FormaPagamento.choices,
    )

    fixa = models.BooleanField(default=False)

    observacao = models.TextField(
        blank=True,
        null=True,
    )

    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'finances_despesa'
        ordering = ['-data', '-id']

    def __str__(self):
        return f'{self.descricao} - R$ {self.valor}'