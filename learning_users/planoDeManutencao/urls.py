from django.conf.urls import url
from . import views

app_name = 'planoDeManutencao'

urlpatterns = [
    #url(r'^$', views.CreatePlanoDeManutencao.as_view(), name='create'),
    url(r'^$', views.create_Plano_Man, name='create'),
]
