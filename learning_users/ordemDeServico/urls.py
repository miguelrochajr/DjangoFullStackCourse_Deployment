from django.conf.urls import url
from . import views

app_name = 'ordemDeServico'

urlpatterns = [
    #url(r'^$', views.CreateOrdemDeServico.as_view(), name='create'),
    url(r'^$', views.create_os, name='create'),
    url(r'success/$', views.SuccessfullyCreateOS.as_view(), name='sucess'),
]
