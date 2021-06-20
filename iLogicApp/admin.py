from django.contrib import admin
from .models import Usuario, Exercicios, Exercicio_Usuario

admin.site.register(Usuario)
admin.site.register(Exercicios)
admin.site.register(Exercicio_Usuario)
