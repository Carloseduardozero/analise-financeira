from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render

from apps.finances.forms.despesa_form import DespesaForm
from apps.finances.selectors.despesa_selector import DespesaSelector
from apps.finances.services.despesa_service import DespesaService


@login_required
def despesa_list_view(request):
    despesas = DespesaSelector.listar_por_usuario(request.user)

    return render(request, 'finances/despesas/list.html', {
        'despesas': despesas,
    })


@login_required
def despesa_create_view(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST, usuario=request.user)

        if form.is_valid():
            try:
                DespesaService.criar_despesa(
                    usuario=request.user,
                    dados=form.cleaned_data,
                )

                messages.success(request, 'Despesa cadastrada com sucesso.')

                return redirect('finances:despesa_list')

            except ValidationError as error:
                form.add_error(None, error.message)
    else:
        form = DespesaForm(usuario=request.user)

    return render(request, 'finances/despesas/form.html', {
        'form': form,
        'titulo': 'Nova despesa',
    })


@login_required
def despesa_update_view(request, despesa_id):
    despesa = DespesaSelector.buscar_por_id_e_usuario(
        despesa_id=despesa_id,
        usuario=request.user,
    )

    if request.method == 'POST':
        form = DespesaForm(
            request.POST,
            instance=despesa,
            usuario=request.user,
        )

        if form.is_valid():
            try:
                DespesaService.atualizar_despesa(
                    despesa=despesa,
                    dados=form.cleaned_data,
                )

                messages.success(request, 'Despesa atualizada com sucesso.')

                return redirect('finances:despesa_list')

            except ValidationError as error:
                form.add_error(None, error.message)
    else:
        form = DespesaForm(instance=despesa, usuario=request.user)

    return render(request, 'finances/despesas/form.html', {
        'form': form,
        'titulo': 'Editar despesa',
    })


@login_required
def despesa_delete_view(request, despesa_id):
    despesa = DespesaSelector.buscar_por_id_e_usuario(
        despesa_id=despesa_id,
        usuario=request.user,
    )

    if request.method == 'POST':
        DespesaService.excluir_despesa(despesa)

        messages.success(request, 'Despesa excluída com sucesso.')

        return redirect('finances:despesa_list')

    return render(request, 'finances/despesas/delete.html', {
        'despesa': despesa,
    })