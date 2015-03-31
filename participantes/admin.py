from django.contrib import admin
from .models import Participante, Pontuacao


class PontuacaoInline(admin.TabularInline):
    model = Pontuacao
    readonly_fields = ('pontos', 'timestamp')

    def has_add_permission(self, *args, **kwargs):
        return False
   
    def has_delete_permission(self, *args, **kwargs):
        return False 

class ParticipanteAdmin(admin.ModelAdmin):
    inlines = [PontuacaoInline]
    list_display = ('nome', 'uri_id')


admin.site.register(Participante, ParticipanteAdmin)

