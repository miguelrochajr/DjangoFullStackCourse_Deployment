from django import forms
from django.forms import formset_factory
from ordemDeServico.models import OrdemDeServico


class OrdemServForm(forms.ModelForm):
    class Meta:
        model = OrdemDeServico
        fields = ["tipo_da_requisicao","divisao","description_brief","unidadeRequisitante","description_full", "planosDeMan"]
