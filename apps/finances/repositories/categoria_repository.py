from apps.finances.models import Categoria

class CategoriaRepository:
    
    @staticmethod
    def criar(usuario, dados):
        return Categoria.objects.create(
            usuario=usuario,
            nome=dados['nome'],
            tipo=dados['tipo'],
            ativa=dados.get('ativa', True),
        )

    @staticmethod
    def atualizar(categoria, dados):
        categoria.nome = dados['nome']
        categoria.tipo = dados['tipo']
        categoria.ativa = dados.get('ativa', False)
        categoria.save()

        return categoria

    @staticmethod
    def excluir(categoria):
        categoria.delete()