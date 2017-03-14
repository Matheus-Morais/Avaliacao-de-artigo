from django.shortcuts import render

from django.http import HttpResponse
from .models import avaliacaoArtigo

def AllAvaliacoes(request):
    lista_avaliacao = avaliacaoArtigo.objects.all()
    retorno = ''
    for artigo in lista_avaliacao:
        retorno += "Id artigo" + str(artigo.id_artigo) + " -- id avaliador = " + str(artigo.id_avaliador) + " -- nota = " + str(artigo.nota) + " -- data = "+ str(artigo.data) +"<br/>"
    return HttpResponse(retorno)

def avaliacaoX(request, id):
    avalicao = avaliacaoArtigo.objects.get(pk = id)
    return HttpResponse("id artigo = " +str(avalicao.id_artigo)+ " -- id avaliador = "+str(avalicao.id_avaliador)+" -- avaliacao = "+str(avalicao.nota)+ " -- data = " +str(avalicao.data))