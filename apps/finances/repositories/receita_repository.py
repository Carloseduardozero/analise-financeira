from apps.finances.models import Receita

class ReceitaRepository:

    @staticmethod
    def criar(usuario, dados):
        return Receita.objects.create(
            usuario=usuario,
            categoria=dados['categoria'],
            descricao=dados['descricao'],
            valor=dados['valor'],
            data=dados['data'],
            origem=dados['origem'],
            observacao=dados.get('observacao'),
        )
    
    @staticmethod
    def atualizar(receita, dados):
        receita.categoria = dados['categoria']
        receita.descricao = dados['descricao']
        receita.valor = dados['valor']
        receita.data = dados['data']
        receita.origem = dados['origem']
        receita.observacao = dados.get('observacao')
        receita.save()

        return receita
    
    @staticmethod
    def excluir(receita):
        receita.delete()