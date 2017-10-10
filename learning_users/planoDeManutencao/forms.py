from django import forms
from django.forms import formset_factory
from planoDeManutencao.models import PlanoDeManutencao
from ordemDeServico.models import OrdemDeServico

fomrsetOrdemDeServico = formset_factory(OrdemDeServico) # Creates a set of OrdemDeServico

class planManForm(forms.ModelForm):
    class Meta:
        model = PlanoDeManutencao
        fields = [ 'especialidade', 'description_full', 'description_brief']
