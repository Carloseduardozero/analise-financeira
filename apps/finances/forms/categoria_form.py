from django import forms

from apps.finances.models import Categoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'tipo', 'ativa']

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Alimentação, Salário, Transporte',
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-select',
            }),
            'ativa': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }