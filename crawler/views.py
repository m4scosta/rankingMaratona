from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from .utils import CrawlerDePontuacao


def atualizar_rankings(request):
    CrawlerDePontuacao().crawl()
    return redirect(reverse('ranking-paricipantes'))
