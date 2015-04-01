from django.shortcuts import render
from crawler.models import RankingUpdate
from participantes.models import Participante, Pontuacao


def ranking_paricipantes(request):
    participantes = filter(lambda p: p.ultima_pontuacao, Participante.objects.all())
    participantes.sort(key=lambda p: p.ultima_pontuacao.pontos, reverse=True)
    context = {
        'participantes': participantes,
        'ultima_atualizacao': RankingUpdate.objects.last()
    }
    return render(request, 'ranking/ranking_participantes.html', context)

