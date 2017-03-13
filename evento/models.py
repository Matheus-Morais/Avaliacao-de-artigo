from django.db import models

from django.db import models
from django.utils import timezone

class avaliacaoArtigo(models.Model):
    id_artigo = models.ForeignKey('id_artigo')
    id_avaliador = models.ForeignKey('id_avaliador')
    nota = models.FloatField('nota')