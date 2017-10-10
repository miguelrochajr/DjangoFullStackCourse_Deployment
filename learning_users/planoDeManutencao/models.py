from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.core.urlresolvers import reverse
import uuid

import misaka # misaka allows us to embbed links into the posts.

from django.contrib.auth import get_user_model #Returns the user model currently active
User = get_user_model() #allow us to call things from this user sessions

#from ordemDeServico.models import OrdemDeServico

# https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/#inclusion-tags
# This is for the in_group_members check template tag
from django import template
register = template.Library()

class PlanoDeManutencao(models.Model):
    # user = models.ForeignKey(User, related_name="planos")
    LISTA_ESPCIALIDADES = (
        ("HD","HIDRAULICA"),
        ("EL","ELETRICA"),
        ("MC", "MACENARIA"),
        ("OU","OUTROS"),
    )
    identifier = models.CharField(max_length=100, unique=True, default=uuid.uuid4, editable=False)
    titleID = models.CharField(max_length=255)
    especialidade = models.CharField(max_length=2, choices=LISTA_ESPCIALIDADES, null=False, default='-')#, verbose_name="Especialidade")
    created_at = models.DateTimeField(auto_now=True)
    frequency = models.IntegerField(unique=False, blank=False, default=0)
    description_full = models.TextField(blank=False, verbose_name="Descrição completa")
    description_brief = models.TextField(max_length=140, blank=False, verbose_name="Descrição breve")

    def __str__(self):
        return self.description_brief

    def save(self, *args, **kwargs):
        # After this, take a look at this Stack overflow post about auto_now https://goo.gl/js6YhE
        print("Save function called!")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("planoDeManutencao:create")

    def set_name(self, chosenEspecialidade):
        self.name = self.name = "{}{}{}".format(chosenEspecialidade, 1111, 444334, 2017)

    def getEspecialidade(self, esp):
        return {
            'HD': LISTA_ESPCIALIDADES[0],
            'EL': LISTA_ESPCIALIDADES[1],
            'MC': LISTA_ESPCIALIDADES[2],
            'OU': LISTA_ESPCIALIDADES[3],
        }[esp]

    class Meta:
        ordering = ['created_at']


# class PlanoPossuiOrdem(models.Model):
#     planoDeManutencao = models.ForeignKey(PlanoDeManutencao, related_name='possuiPlano')
#     ordemDeServico = models.ForeignKey(OrdemDeServico, related_name='plano_ordens')
