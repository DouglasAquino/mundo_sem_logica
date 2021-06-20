from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home, exercicios, cadastrar, AcessarExercio, Salvar, ant, prox, revista

urlpatterns = [
    path('',home,name="home"),
    path('exercicios',exercicios,name="exercicios"),
    path('cadastrar',cadastrar,name="cadastrar"),
    path('Salvar/<int:id>/<int:p>',Salvar,name="Salvar"),
    path('AcessarExercio/<int:id>',AcessarExercio,name="AcessarExercio"),
    path('ant/<int:id>',ant,name="ant"),
    path('prox/<int:id>',prox,name="prox"),
    path('revista',revista,name="revista"),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
