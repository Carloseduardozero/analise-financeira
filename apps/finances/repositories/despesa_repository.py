from apps.finances.models import Despesa


class DespesaRepository:
    @staticmethod
    def criar(usuario, dados):
        return Despesa.objects.create(
            usuario=usuario,
            categoria=dados['categoria'],
            descricao=dados['descricao'],
            valor=dados['valor'],
            data=dados['data'],
            forma_pagamento=dados['forma_pagamento'],
            fixa=dados.get('fixa', False),
            observacao=dados.get('observacao'),
        )

    @staticmethod
    def atualizar(despesa, dados):
        despesa.categoria = dados['categoria']
        despesa.descricao = dados['descricao']
        despesa.valor = dados['valor']
        despesa.data = dados['data']
        despesa.forma_pagamento = dados['forma_pagamento']
        despesa.fixa = dados.get('fixa', False)
        despesa.observacao = dados.get('observacao')
        despesa.save()

        return despesa

    @staticmethod
    def excluir(despesa):
        despesa.delete()