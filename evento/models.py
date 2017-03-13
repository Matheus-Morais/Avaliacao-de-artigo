from django.db import models

from django.db import models
from django.utils import timezone

class avaliacaoArtigo(models.Model):
    id_artigo = models.IntegerField('id_artigo')
    id_avaliador = models.IntegerField('id_avaliador')
    nota = models.FloatField('nota')