from django.shortcuts import render

from django.http import HttpResponse
from .models import avaliacaoArtigo

def AvaliarArtigo(request, id_artigo, id_avaliador, nota):
    avaliacao = avaliacaoArtigo(id_artigo, id_avaliador, nota)
    #avaliacao.id_avaliador = id_avaliador
    #avaliacao.id_artigo = id_artigo
    #avaliacao.nota = nota
    avaliacao.add()
    return HttpResponse("tudo certo")

def AllAvaliacoes(request):
    lista_avaliacao = avaliacaoArtigo.objects.all()
    retorno = ''
    for artigo in lista_avaliacao:
        retorno += "<li>" + artigo.id_artigo + " / " + artigo.id_avaliador + " / " + artigo.nota + " / </li>"
    return HttpResponse(retorno)

def avaliacaoX(request, id):
    avalicao = avaliacaoArtigo.objects(pk = id)
    return HttpResponse("id artigo = " +avalicao.id_artigo+ " -- id avaliador = "+avalicao.id_avaliador+" -- avaliacao = "+avalicao.nota)