from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Agendamento, Servico
from datetime import timedelta
from django.utils import timezone
from django.db.models import Sum

def novo_agendamento(request):
    if request.method == "POST":
        servicos_selecionados = request.POST.getlist('servicos')
        data_desejada_str = request.POST.get('data_hora')
        cliente_nome = request.POST.get('cliente_nome')
        telefone = request.POST.get('telefone')
        profissional = request.POST.get('profissional')
        
        confirmado = request.POST.get('confirmar_duplicado') == 'true'

        if not data_desejada_str or not servicos_selecionados or not cliente_nome:
            messages.error(request, "Preencha todos os campos obrigatórios.")
            return render(request, 'agendamentos/form_agendamento.html', {'servicos': Servico.objects.all()})

        try:
            data_desejada = timezone.datetime.fromisoformat(data_desejada_str)
        except (ValueError, TypeError):
            messages.error(request, "Formato de data inválido.")
            return redirect('novo_agendamento')

        inicio_semana = data_desejada.date() - timedelta(days=data_desejada.weekday())
        fim_semana = inicio_semana + timedelta(days=6)
        existente = Agendamento.objects.filter(
            cliente_nome__iexact=cliente_nome,
            data_hora__date__range=[inicio_semana, fim_semana]
        ).first()

        if existente and existente.data_hora.date() != data_desejada.date() and not confirmado:
            data_fmt = existente.data_hora.strftime('%d/%m')
            messages.warning(request, f"AVISO: {cliente_nome} já tem horário em {data_fmt}. Deseja manter?")
            return render(request, 'agendamentos/form_agendamento.html', {
                'servicos': Servico.objects.all(),
                'aviso_duplicado': True,
                'dados': request.POST,
                'servicos_selecionados': servicos_selecionados
            })

        novo = Agendamento.objects.create(
            cliente_nome=cliente_nome,
            telefone=telefone,
            profissional=profissional,
            data_hora=data_desejada
        )
        novo.servicos.set(servicos_selecionados)
        messages.success(request, f"Agendamento de {cliente_nome} realizado!")
        return redirect('historico_agendamentos')

    return render(request, 'agendamentos/form_agendamento.html', {'servicos': Servico.objects.all()})

def historico_agendamentos(request):
    agendamentos_base = Agendamento.objects.all().order_by('-data_hora')
    
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    if data_inicio and data_fim:
        data_fim_obj = timezone.datetime.fromisoformat(data_fim) + timedelta(days=1)
        agendamentos_base = agendamentos_base.filter(data_hora__range=[data_inicio, data_fim_obj])

    confirmados = agendamentos_base.filter(status='CONFIRMADO')
    total_faturado = 0
    total_servicos = 0
    for agm in confirmados:
        total_faturado += agm.servicos.aggregate(total=Sum('preco'))['total'] or 0
        total_servicos += agm.servicos.count()

    return render(request, 'agendamentos/historico.html', {
        'agendamentos': agendamentos_base,
        'total_faturado': total_faturado,
        'total_servicos': total_servicos
    })

def alterar_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    if timezone.now() > (agendamento.data_hora - timedelta(days=2)):
        messages.error(request, "Alteração bloqueada (menos de 2 dias).")
        return redirect('historico_agendamentos')

    if request.method == "POST":
        agendamento.cliente_nome = request.POST.get('cliente_nome')
        agendamento.telefone = request.POST.get('telefone')
        agendamento.profissional = request.POST.get('profissional')
        data_str = request.POST.get('data_hora')
        if data_str: agendamento.data_hora = timezone.datetime.fromisoformat(data_str)
        agendamento.servicos.set(request.POST.getlist('servicos'))
        agendamento.save()
        messages.success(request, "Atualizado!")
        return redirect('historico_agendamentos')

    return render(request, 'agendamentos/editar_agendamento.html', {
        'agendamento': agendamento, 'servicos': Servico.objects.all()
    })

def excluir_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    if request.method == "POST":
        agendamento.delete()
        messages.success(request, "Agendamento excluído!")
    return redirect('historico_agendamentos')

def atualizar_status(request, pk):
    if request.method == "POST":
        agendamento = get_object_or_404(Agendamento, pk=pk)
        agendamento.status = request.POST.get('status')
        agendamento.save()
    return redirect('historico_agendamentos')