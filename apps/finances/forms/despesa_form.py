from django import forms

from apps.finances.enums import TipoCategoria
from apps.finances.models import Categoria, Despesa


class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = [
            'descricao',
            'valor',
            'data',
            'categoria',
            'forma_pagamento',
            'fixa',
            'observacao',
        ]

        widgets = {
            'descricao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Mercado, aluguel, internet',
            }),
            'valor': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
            }),
            'data': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select',
            }),
            'forma_pagamento': forms.Select(attrs={
                'class': 'form-select',
            }),
            'fixa': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'observacao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
        }

    def __init__(self, *args, usuario=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['categoria'].queryset = Categoria.objects.filter(
            usuario=usuario,
            tipo=TipoCategoria.DESPESA,
            ativa=True,
        )