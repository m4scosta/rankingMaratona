# coding: utf-8
from django.db import models


class Participante(models.Model):
    nome = models.CharField(max_length=100)
    uri_id = models.PositiveIntegerField()

    class Meta:
        app_label = 'participantes'

    def __unicode__(self):
        return self.nome

    @property
    def ultima_pontuacao(self):
        return self.pontuacoes.last()

    def tem_pontuacao(self):
        return self.pontuacoes.exists()


class Pontuacao(models.Model):
    participante = models.ForeignKey(Participante, related_name='pontuacoes')
    pontos = models.PositiveIntegerField()
    tentados = models.PositiveIntegerField(null=True, blank=True)
    submissoes = models.PositiveIntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'participantes'
        verbose_name = u'pontuação'
        verbose_name_plural = u'pontuações'

    def __unicode__(self):
        return unicode(self.pontos)
