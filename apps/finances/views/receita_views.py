from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render

from apps.finances.forms.receita_form import ReceitaForm
from apps.finances.selectors.receita_selector import ReceitaSelector
from apps.finances.services.receita_service import ReceitaService


@login_required
def receita_list_view(request):
    receitas = ReceitaSelector.listar_por_usuario(request.user)

    return render(request, 'finances/receitas/list.html', {
        'receitas': receitas,
    })


@login_required
def receita_create_view(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST, usuario=request.user)

        if form.is_valid():
            try:
                ReceitaService.criar_receita(
                    usuario=request.user,
                    dados=form.cleaned_data,
                )

                messages.success(request, 'Receita cadastrada com sucesso.')

                return redirect('finances:receita_list')

            except ValidationError as error:
                form.add_error(None, error.message)
    else:
        form = ReceitaForm(usuario=request.user)

    return render(request, 'finances/receitas/form.html', {
        'form': form,
        'titulo': 'Nova receita',
    })


@login_required
def receita_update_view(request, receita_id):
    receita = ReceitaSelector.buscar_por_id_e_usuario(
        receita_id=receita_id,
        usuario=request.user,
    )

    if request.method == 'POST':
        form = ReceitaForm(
            request.POST,
            instance=receita,
            usuario=request.user,
        )

        if form.is_valid():
            try:
                ReceitaService.atualizar_receita(
                    receita=receita,
                    dados=form.cleaned_data,
                )

                messages.success(request, 'Receita atualizada com sucesso.')

                return redirect('finances:receita_list')

            except ValidationError as error:
                form.add_error(None, error.message)
    else:
        form = ReceitaForm(instance=receita, usuario=request.user)

    return render(request, 'finances/receitas/form.html', {
        'form': form,
        'titulo': 'Editar receita',
    })


@login_required
def receita_delete_view(request, receita_id):
    receita = ReceitaSelector.buscar_por_id_e_usuario(
        receita_id=receita_id,
        usuario=request.user,
    )

    if request.method == 'POST':
        ReceitaService.excluir_receita(receita)

        messages.success(request, 'Receita excluída com sucesso.')

        return redirect('finances:receita_list')

    return render(request, 'finances/receitas/delete.html', {
        'receita': receita,
    })