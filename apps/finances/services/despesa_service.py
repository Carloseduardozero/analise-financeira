from django.core.exceptions import ValidationError

from apps.finances.enums import TipoCategoria
from apps.finances.repositories.despesa_repository import DespesaRepository


class DespesaService:
    @staticmethod
    def criar_despesa(usuario, dados):
        DespesaService.validar_categoria(usuario, dados['categoria'])

        return DespesaRepository.criar(usuario, dados)

    @staticmethod
    def atualizar_despesa(despesa, dados):
        DespesaService.validar_categoria(despesa.usuario, dados['categoria'])

        return DespesaRepository.atualizar(despesa, dados)

    @staticmethod
    def excluir_despesa(despesa):
        return DespesaRepository.excluir(despesa)

    @staticmethod
    def validar_categoria(usuario, categoria):
        if categoria.usuario != usuario:
            raise ValidationError('Categoria inválida para este usuário.')

        if categoria.tipo != TipoCategoria.DESPESA:
            raise ValidationError('A categoria precisa ser do tipo despesa.')

        if not categoria.ativa:
            raise ValidationError('A categoria está inativa.')