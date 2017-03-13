from django.db import models

from django.db import models
from django.utils import timezone

class avaliacaoArtigo(models.Model):
    id_evento = models.IntegerField('id_evento')
    id_avaliador = models.IntegerField('id_avaliador')
    nota = models.FloatField('nota')