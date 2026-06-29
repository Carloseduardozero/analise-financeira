from django.core.exceptions import ValidationError

from apps.finances.models import Categoria
from apps.finances.repositories.categoria_repository import CategoriaRepository


class CategoriaService:
    
    @staticmethod
    def criar_categoria(usuario, dados):
        CategoriaService.validar_categoria_duplicada(
            usuario=usuario,
            nome=dados['nome'],
            tipo=dados['tipo'],
        )

        return CategoriaRepository.criar(usuario, dados)

    @staticmethod
    def atualizar_categoria(categoria, dados):
        CategoriaService.validar_categoria_duplicada(
            usuario=categoria.usuario,
            nome=dados['nome'],
            tipo=dados['tipo'],
            categoria_id=categoria.id,
        )

        return CategoriaRepository.atualizar(categoria, dados)

    @staticmethod
    def excluir_categoria(categoria):
        return CategoriaRepository.excluir(categoria)

    @staticmethod
    def validar_categoria_duplicada(usuario, nome, tipo, categoria_id=None):
        query = Categoria.objects.filter(
            usuario=usuario,
            nome__iexact=nome,
            tipo=tipo,
        )

        if categoria_id:
            query = query.exclude(id=categoria_id)

        if query.exists():
            raise ValidationError(
                'Já existe uma categoria com esse nome e tipo.'
            )