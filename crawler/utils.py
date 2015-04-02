# coding: utf-8
import re
import urllib2
from crawler.models import RankingUpdate

from participantes.models import Participante, Pontuacao


class CrawlerDePontuacao(object):
    URI_PROFILE_URL = 'https://www.urionlinejudge.com.br/judge/pt/profile/%d'
    POINTS_PATTERN = re.compile(r'<span>Resolvido:</span>(\d+)')
    TRIED_PATTERN = re.compile(r'<span>Tentado:</span>(\d+)')
    SUBMISSIONS_PATTERN = re.compile(r'<span>Submissões:</span>(\d+)')

    def get_participantes(self):
        return Participante.objects.all()

    def crawl(self):
        for participante in self.get_participantes():
            html_content = self.get_profile_html_content(participante)
            points = self.parse_points(html_content)
            tried = self.parse_tried(html_content)
            submissions = self.parse_submissions(html_content)

            if not participante.tem_pontuacao() or \
                    participante.ultima_pontuacao.pontos != points or \
                    participante.ultima_pontuacao.tentados != tried or \
                    participante.ultima_pontuacao.submissoes != submissions:
                Pontuacao.objects.create(
                    participante=participante, pontos=points, tentados=tried, submissoes=submissions
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

    def parse_tried(self, html_content):
        try:
            return self.TRIED_PATTERN.search(html_content).groups()[0]
        except Exception as e:
            print e

    def parse_submissions(self, html_content):
        try:
            return self.SUBMISSIONS_PATTERN.search(html_content).groups()[0]
        except Exception as e:
            print e

    @staticmethod
    def save_ranking_update():
        RankingUpdate().save()
