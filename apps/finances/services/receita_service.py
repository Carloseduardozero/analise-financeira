from django.core.exceptions import ValidationError

from apps.finances.enums import TipoCategoria
from apps.finances.repositories.receita_repository import ReceitaRepository

class ReceitaService:

    @staticmethod
    def criar_receita(usuario, dados):
        ReceitaService.validar_categoria(usuario, dados['categoria'])

        return ReceitaRepository.criar(usuario, dados)

    @staticmethod
    def atualizar_receita(receita, dados):
        ReceitaService.validar_categoria(receita.usuario, dados['categoria'])

        return ReceitaRepository.atualizar(receita, dados)

    @staticmethod
    def excluir_receita(receita):
        return ReceitaRepository.excluir(receita)

    @staticmethod
    def validar_categoria(usuario, categoria):
        if categoria.usuario != usuario:
            raise ValidationError('Categoria inválida para este usuário.')

        if categoria.tipo != TipoCategoria.RECEITA:
            raise ValidationError('A categoria precisa ser do tipo receita.')

        if not categoria.ativa:
            raise ValidationError('A categoria está inativa.')