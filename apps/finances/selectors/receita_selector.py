from django.shortcuts import get_object_or_404

from apps.finances.models import Receita

class ReceitaSelector:
    
    @staticmethod
    def listar_por_usuario(usuario):
        return Receita.objects.filter(
            usuario=usuario,
        ).select_related('categoria')

    @staticmethod
    def buscar_por_id_e_usuario(receita_id, usuario):
        return get_object_or_404(
            Receita.objects.select_related('categoria'),
            id=receita_id,
            usuario=usuario,
        )