from django.db import models


class FormaPagamento(models.TextChoices):
    PIX = 'PIX', 'PIX'
    DINHEIRO = 'DINHEIRO', 'Dinheiro'
    CARTAO_CREDITO = 'CARTAO_CREDITO', 'Cartão de crédito'
    CARTAO_DEBITO = 'CARTAO_DEBITO', 'Cartão de débito'
    BOLETO = 'BOLETO', 'Boleto'
    TRANSFERENCIA = 'TRANSFERENCIA', 'Transferência'
    OUTROS = 'OUTROS', 'Outros'