# coding: utf-8
import re
import urllib2
from crawler.models import RankingUpdate

from participantes.models import Participante, Pontuacao


class CrawlerDePontuacao(object):
    URI_PROFILE_URL = 'https://www.urionlinejudge.com.br/judge/pt/profile/%d'
    POINTS_PATTERN = re.compile(r'<span>Resolvido:</span>(\d+)')

    def get_participantes(self):
        return Participante.objects.all()

    def crawl(self):
        for participante in self.get_participantes():
            html_content = self.get_profile_html_content(participante)
            points = self.parse_points(html_content)

            if not participante.tem_pontuacao() or \
                    participante.ultima_pontuacao.pontos != points:
                Pontuacao.objects.create(
                    participante=participante, pontos=points
                )
        self.save_ranking_update()

    def get_profile_html_content(self, participante):
        url = self.URI_PROFILE_URL % participante.uri_id
        return urllib2.urlopen(url).read()

    def parse_points(self, html_content):
        try:
            return self.POINTS_PATTERN.search(html_content).groups()[0]
        except Exception as e:
            print e

    @staticmethod
    def save_ranking_update():
        RankingUpdate().save()
