from django.db import models

class TipoCategoria(models.TextChoices):
    RECEITA = 'RECEITA', 'Receita'
    DESPESA = 'DESPESA', 'Despesa'