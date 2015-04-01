# coding: utf-8
import re
import urllib2

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
            if participante.ultima_pontuacao != points:
                Pontuacao.objects.create(
                    participante=participante, pontos=points
                )

    def get_profile_html_content(self, participante):
        url = self.URI_PROFILE_URL % participante.uri_id
        return urllib2.urlopen(url).read()

    def parse_points(self, html_content):
        try:
            return self.POINTS_PATTERN.search(html_content).groups()[0]
        except Exception as e:
            print e
