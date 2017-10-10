from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views import generic

from braces.views import SelectRelatedMixin

from planoDeManutencao import models
from planoDeManutencao import forms

from django.contrib.auth import get_user_model
User = get_user_model()

class CreatePlanoDeManutencao(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    model = models.PlanoDeManutencao
    fields = ('especialidade','description_full', 'description_brief')

    # def __init__(self,*args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["ordensDeServico"].label = "Ordens de Serviço Cadastradas"
    #     self.fields["description_brief"].label = "Descrição breve"
    #     self.fields["description_full"].label = "Descrição Completa"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

def create_Plano_Man(request):
    form = forms.planManForm()

    if request.method == 'POST':
        form = forms.planManForm(request.POST)
        if form.is_valid():

            planMan = form.save(commit=False) #Grab the actual model from the form
            planMan.save() #Save this actual model to produce a primary key
            print("My PK is: {}".format(planMan.pk))

            pk_str = str(planMan.pk) # primary key string representation
            if len(pk_str) < 5:
                pk_str = pk_str.zfill(5) #Padding pk_str with zeros

            created_date = str(planMan.created_at).split('-')[0] # Grab the year

            # Updating the model
            planMan.titleID = "{}{}{}".format(planMan.especialidade, pk_str, created_date)
            planMan.save() # save modified model

            print("Created date: " + str(planMan.created_at))
            print("Especialidade: " + form.cleaned_data['especialidade'])
            print("Frequência: " + str(form.cleaned_data['frequency']))
            print("Descrição completa: " + form.cleaned_data['description_full'])
            print("Descrição breve: " + form.cleaned_data['description_brief'])

    return render(request, 'planoDeManutencao/planodemanutencao_form.html',
                        {'form':form})
