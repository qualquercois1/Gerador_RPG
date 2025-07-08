# generator/urls.py

from django.urls import path
from . import views  # O "." importa as views da pasta atual

# Este é um nome padrão do Django, não mude
urlpatterns = [
    # Quando alguém acessar a URL raiz da nossa app,
    # chame a função 'home_view' que está no arquivo views.py.
    # O 'name' é um apelido para a rota, muito útil!
    path('', views.home_view, name='home'),
]