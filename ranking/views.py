from django.shortcuts import render
from participantes.models import Participante


def ranking_paricipantes(request):
    participantes = list(Participante.objects.all())
    participantes.sort(key=lambda p: p.ultima_pontuacao.pontos, reverse=True)
    context = {'participantes': participantes}
    return render(request, 'ranking/ranking_participantes.html', context)

