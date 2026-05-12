from django.contrib import admin
from .models import Agendamento, Servico   
from django.utils import timezone
from datetime import timedelta
from django.db.models import Sum

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'duracao_minutos')
    search_fields = ('nome',)

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente_nome', 'profissional', 'data_hora', 'status', 'telefone', 'pode_alterar_pelo_sistema')
    list_filter = ('status', 'data_hora', 'profissional')
    search_fields = ('cliente_nome', 'telefone')
    actions = ['confirmar_agendamentos']

    def confirmar_agendamentos(self, request, queryset):
        queryset.update(status='CONFIRMADO')
    confirmar_agendamentos.short_description = "Confirmar agendamentos selecionados"


    def changelist_view(self, request, extra_context=None):
        hoje = timezone.now().date()
        inicio_semana = hoje - timedelta(days=hoje.weekday())
        agendamentos_semana = Agendamento.objects.filter(data_hora__date__gte=inicio_semana)
        
        total_receita = 0
        for agendamento in agendamentos_semana:
            soma = agendamento.servicos.aggregate(Sum('preco'))['preco__sum']
            if soma:
                total_receita += soma

        extra_context = extra_context or {}
        extra_context['total_semana'] = agendamentos_semana.count()
        extra_context['receita_semana'] = total_receita
        return super().changelist_view(request, extra_context=extra_context)