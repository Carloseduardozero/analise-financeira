from django.shortcuts import get_object_or_404

from apps.finances.models import Categoria

class CategoriaSelector:
    @staticmethod
    def listar_por_usuario(usuario):
        return Categoria.objects.filter(usuario=usuario)

    @staticmethod
    def buscar_por_id_e_usuario(categoria_id, usuario):
        return get_object_or_404(
            Categoria,
            id=categoria_id,
            usuario=usuario,
        )