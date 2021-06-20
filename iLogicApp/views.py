from django.shortcuts import redirect, render
from .models import Usuario, Exercicios, Exercicio_Usuario
from django.contrib.auth.models import User

def home(request):
    usuario = None
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(user=request.user)
    return render(request, 'home.html', {"usuario":usuario})

def exercicios(request):
    if request.user.is_authenticated:
        usuario=Usuario.objects.get(user=request.user)
        exer = Exercicios.objects.all()
        lista=[]
        for e in exer:
            ex=[]
            ex.append(e)
            if Exercicio_Usuario.objects.filter(usuario=usuario,exercicio=e):
                eu = Exercicio_Usuario.objects.get(usuario=usuario,exercicio=e)
                ex.append(eu)
            else:
                ex.append("Bloqueado")
            lista.append(ex)
        return render(request, 'controle.html', {"exercicios":lista})
    else:
        msg="VOCÊ PRECISA ESTÁ LOGADO PARA CONTINUAR"
        return render(request, 'erro.html', {'msg':msg})

def cadastrar(request):
    if not request.user.is_authenticated:
        pass
    else:
        return redirect('login')

def AcessarExercio(request,id):
    if request.user.is_authenticated:
        usuario=Usuario.objects.get(user=request.user)
        if Exercicio_Usuario.objects.filter(usuario=usuario,exercicio__pk=id):
            exer = Exercicio_Usuario.objects.get(usuario=usuario,exercicio__pk=id)
        elif Exercicios.objects.filter(pk=id):
            exer = Exercicio_Usuario()
            exer.usuario = usuario
            exer.exercicio = Exercicios.objects.get(pk=id)
            exer.save()
        else:
            msg="Desculpe, exercício ainda não cadastrado!"
            return render(request, 'erro.html', {'msg':msg})
        return render(request, exer.exercicio.pag, {'exercicio':exer,'msg':None})
    else:
        msg="VOCÊ PRECISA ESTÁ LOGADO PARA CONTINUAR"
        return render(request, 'erro.html', {'msg':msg})

def Salvar(request,id,p):
    if request.user.is_authenticated:
        usuario=Usuario.objects.get(user=request.user)
        exercicio = Exercicios.objects.get(pk=id)
        eu = Exercicio_Usuario.objects.get(usuario=usuario,exercicio=exercicio)
        eu.pontos = p
        eu.status = '1'
        eu.save()
        return AcessarExercio(request,id+1)
    else:
        msg="VOCÊ PRECISA ESTÁ LOGADO PARA CONTINUAR"
        return render(request, 'erro.html', {'msg':msg})

def prox(request,id):
    return redirect("AcessarExercio",id+1)
def ant(request,id):
    return redirect("AcessarExercio",id-1)

def revista(request):
    msg="EM BREVE O QUADRINHO DO MUNDO SEM LÓGICA"
    return render(request, 'erro.html', {'msg':msg})