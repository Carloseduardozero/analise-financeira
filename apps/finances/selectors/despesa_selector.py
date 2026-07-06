from django.shortcuts import get_object_or_404

from apps.finances.models import Despesa


class DespesaSelector:
    @staticmethod
    def listar_por_usuario(usuario):
        return Despesa.objects.filter(
            usuario=usuario,
        ).select_related('categoria')

    @staticmethod
    def buscar_por_id_e_usuario(despesa_id, usuario):
        return get_object_or_404(
            Despesa.objects.select_related('categoria'),
            id=despesa_id,
            usuario=usuario,
        )