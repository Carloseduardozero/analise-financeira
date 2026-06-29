from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render

from apps.finances.forms.categoria_form import CategoriaForm
from apps.finances.selectors.categoria_selector import CategoriaSelector
from apps.finances.services.categoria_service import CategoriaService


@login_required
def categoria_list_view(request):
    categorias = CategoriaSelector.listar_por_usuario(request.user)

    return render(request, 'finances/categorias/list.html', {
        'categorias': categorias,
    })


@login_required
def categoria_create_view(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)

        if form.is_valid():
            try:
                CategoriaService.criar_categoria(
                    usuario=request.user,
                    dados=form.cleaned_data,
                )

                messages.success(request, 'Categoria cadastrada com sucesso.')

                return redirect('finances:categoria_list')

            except ValidationError as error:
                form.add_error(None, error.message)
    else:
        form = CategoriaForm()

    return render(request, 'finances/categorias/form.html', {
        'form': form,
        'titulo': 'Nova categoria',
    })


@login_required
def categoria_update_view(request, categoria_id):
    categoria = CategoriaSelector.buscar_por_id_e_usuario(
        categoria_id=categoria_id,
        usuario=request.user,
    )

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)

        if form.is_valid():
            try:
                CategoriaService.atualizar_categoria(
                    categoria=categoria,
                    dados=form.cleaned_data,
                )

                messages.success(request, 'Categoria atualizada com sucesso.')

                return redirect('finances:categoria_list')

            except ValidationError as error:
                form.add_error(None, error.message)
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, 'finances/categorias/form.html', {
        'form': form,
        'titulo': 'Editar categoria',
    })


@login_required
def categoria_delete_view(request, categoria_id):
    categoria = CategoriaSelector.buscar_por_id_e_usuario(
        categoria_id=categoria_id,
        usuario=request.user,
    )

    if request.method == 'POST':
        CategoriaService.excluir_categoria(categoria)

        messages.success(request, 'Categoria excluída com sucesso.')

        return redirect('finances:categoria_list')

    return render(request, 'finances/categorias/delete.html', {
        'categoria': categoria,
    })