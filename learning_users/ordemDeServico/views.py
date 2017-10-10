from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from . import forms
from . import models

from django.contrib.auth import get_user_model
User = get_user_model()


class CreateOrdemDeServico(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):

    model = models.OrdemDeServico
    fields = ("number","tipo_da_requisicao","divisao","description_brief","unidadeRequisitante","description_full")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class SuccessfullyCreateOS(generic.TemplateView):
    template_name = "ordemDeServico/ordemCriada.html"


def create_os(request):
    form = forms.OrdemServForm()
    if request.method == 'POST':
        form = forms.OrdemServForm(request.POST)
        if form.is_valid():
            print("FORM VALIDATED!")
            os = form.save(commit=False) # Grab the actual model from the form
            os.status = 'ESPERANDO REVISÃO'
            os.save() # Save this actual model to produce a primary key
            return render(request, 'ordemDeServico/ordemCriada.html')

    return render(request, 'ordemDeServico/ordemdeservico_form.html', {'form': form})
