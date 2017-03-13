from django.shortcuts import render

from django.http import HttpResponse
from .models import avaliacaoArtigo

def AvaliarArtigo(request, id_artigo, id_avaliador, nota):

    return

def AllAvaliacoes(request):
    lista_avaliacao = avaliacaoArtigo.objects.all()
    retorno = ''
    for artigo in lista_avaliacao:
        retorno += "<li>" + artigo.id_evento + " / " + artigo.id_avaliador + " / " + artigo.nota + " / </li>"
    return HttpResponse(retorno)