from django.urls import path

from apps.finances.views.categoria_views import (
    categoria_create_view,
    categoria_delete_view,
    categoria_list_view,
    categoria_update_view,
)

from apps.finances.views.despesa_views import (
    despesa_create_view,
    despesa_delete_view,
    despesa_list_view,
    despesa_update_view,
)

from apps.finances.views.receita_views import (
    receita_create_view,
    receita_delete_view,
    receita_list_view,
    receita_update_view,
)

app_name = 'finances'

urlpatterns = [
    path('categorias/', categoria_list_view, name='categoria_list'),
    path('categorias/nova/', categoria_create_view, name='categoria_create'),
    path('categorias/<int:categoria_id>/editar/', categoria_update_view, name='categoria_update'),
    path('categorias/<int:categoria_id>/excluir/', categoria_delete_view, name='categoria_delete'),

    path('despesas/', despesa_list_view, name='despesa_list'),
    path('despesas/nova/', despesa_create_view, name='despesa_create'),
    path('despesas/<int:despesa_id>/editar/', despesa_update_view, name='despesa_update'),
    path('despesas/<int:despesa_id>/excluir/', despesa_delete_view, name='despesa_delete'),

    path('receitas/', receita_list_view, name='receita_list'),
    path('receitas/nova/', receita_create_view, name='receita_create'),
    path('receitas/<int:receita_id>/editar/', receita_update_view, name='receita_update'),
    path('receitas/<int:receita_id>/excluir/', receita_delete_view, name='receita_delete'),
]