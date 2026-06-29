from django.conf import settings
from django.db import models
from apps.finances.enums import TipoCategoria


class Categoria(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='categorias',
    )

    nome = models.CharField(max_length=100)

    tipo = models.CharField(
        max_length=20,
        choices=TipoCategoria.choices,
    )

    ativa = models.BooleanField(default=True)

    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'finances_categoria'
        ordering = ['nome']
        constraints = [
            models.UniqueConstraint(
                fields=['usuario', 'nome', 'tipo'],
                name='unique_categoria_por_usuario_nome_tipo',
            )
        ]

    def __str__(self):
        return f'{self.nome} ({self.get_tipo_display()})'