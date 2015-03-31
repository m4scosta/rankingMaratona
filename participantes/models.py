# coding: utf-8
from django.db import models


class Participante(models.Model):
    nome = models.CharField(max_length=100)
    uri_id = models.PositiveIntegerField()

    class Meta:
        app_label = 'participantes'
    
    def __unicode__(self):
        return self.nome



class Pontuacao(models.Model):
    participante = models.ForeignKey(Participante)
    pontos = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'participantes'
        verbose_name = u'pontuação'
        verbose_name_plural = u'pontuações'

