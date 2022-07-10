from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    # return HttpResponse("teste")
    return render(request, 'cadastro.html') 

def logar(request):
    return HttpResponse("Voce esta na pagina de login")


