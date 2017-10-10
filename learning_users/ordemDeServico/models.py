from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.core.urlresolvers import reverse

import misaka # misaka allows us to embbed links into the posts.

from django.contrib.auth import get_user_model #Returns the user model currently active
User = get_user_model() #allow us to call things from this user sessions

# https://docs.djangoproject.com/en/1.11/howto/custom-template-tags/#inclusion-tags
# This is for the in_group_members check template tag
from django import template
register = template.Library()

from planoDeManutencao.models import PlanoDeManutencao

class OrdemDeServico(models.Model):
    TIPO_OS = (
        ("CO","CORRETIVA"),
        ("PR","PREVENTIVA"),
    )

    # number: it is being used as the primary key. TODO: CONFORM THIS AS THE SIPAC ONE
    tipo_da_requisicao = models.CharField(max_length=40, choices=TIPO_OS, null=False, blank=False)
    divisao = models.CharField(max_length=100, default='none')
    # user = models.ForeignKey(User, related_name='created_by')
    created_at = models.DateTimeField(auto_now=True) #Automatically saves the time
    status = models.CharField(max_length=40, default='none')
    unidadeRequisitante = models.CharField(max_length=80, default='none')
    description_full = models.TextField(blank=False)
    description_brief = models.TextField(max_length=140, blank=False)
    planosDeMan = models.ForeignKey(PlanoDeManutencao, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.description_brief

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # kwargs={'number':number} will be done to see the Ordem just created
        return reverse("ordemDeServico:sucess")

    class Meta:
        ordering = ['created_at']
