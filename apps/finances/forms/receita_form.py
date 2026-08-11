from django import forms

from apps.finances.enums import TipoCategoria
from apps.finances.models import Categoria, Receita

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = [
            'descricao',
            'valor',
            'data',
            'categoria',
            'origem',
            'observacao',
        ]

        widgets = {
            'descricao': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Salário, venda, bônus',
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
            'origem': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Empresa, cliente, banco',
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
            tipo=TipoCategoria.RECEITA,
            ativa=True,
        )