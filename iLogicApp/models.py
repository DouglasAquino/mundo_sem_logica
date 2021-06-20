from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nome = models.CharField("Nome",max_length=75)
    foto = models.ImageField("Foto perfil",upload_to='static/imagens',null=True,blank=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Exercicios(models.Model):
    titulo = models.CharField("Titulo", max_length=150)
    pag = models.CharField("Pagina do Exercicio",max_length=150,null=True,blank=True)

    def __str__(self):
        return self.titulo

class Exercicio_Usuario(models.Model):
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    exercicio = models.ForeignKey(Exercicios, on_delete=models.CASCADE)
    pontos = models.IntegerField("Pontos", default=0)
    status_choices=(("0","Aberto"),("1","Concluido"))
    status = models.CharField("Status",choices=status_choices, max_length=30, default="0")

    def __str__(self):
        return '{} - {}'.format(self.usuario.nome,self.exercicio.titulo)