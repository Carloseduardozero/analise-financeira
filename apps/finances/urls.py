from django.urls import path

from apps.finances.views.categoria_views import (
    categoria_create_view,
    categoria_delete_view,
    categoria_list_view,
    categoria_update_view,
)

app_name = 'finances'

urlpatterns = [
    path('categorias/', categoria_list_view, name='categoria_list'),
    path('categorias/nova/', categoria_create_view, name='categoria_create'),
    path('categorias/<int:categoria_id>/editar/', categoria_update_view, name='categoria_update'),
    path('categorias/<int:categoria_id>/excluir/', categoria_delete_view, name='categoria_delete'),
]