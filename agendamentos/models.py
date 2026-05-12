from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    duracao_minutos = models.PositiveIntegerField(help_text="Duração estimada em minutos")

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('CONFIRMADO', 'Confirmado'),
        ('CONCLUIDO', 'Concluído'),
        ('CANCELADO', 'Cancelado'),
    ]

    PROFISSIONAIS_CHOICES = [
        ('victoria', 'Victoria'),
        ('adriana', 'Adriana'),
        ('josiane', 'Josiane'),
        ('rosangela', 'Rosangela'),
        ('camila', 'Camila'),
    ]

    cliente = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='meus_agendamentos', 
        null=True, 
        blank=True
    )
    
    cliente_nome = models.CharField(max_length=150, verbose_name="Nome do Cliente")
    
    telefone = models.CharField(
        max_length=20, 
        verbose_name="Telefone", 
        null=True, 
        blank=True
    )
    
    profissional = models.CharField(max_length=50, choices=PROFISSIONAIS_CHOICES, verbose_name="Profissional")
    
    data_hora = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE')
    servicos = models.ManyToManyField(Servico, related_name='agendamentos')
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.cliente_nome} - {self.data_hora.strftime('%d/%m/%Y %H:%M')}"

    @property
    def pode_alterar_pelo_sistema(self):
        agora = timezone.now()
        prazo_limite = self.data_hora - timedelta(days=2)
        return agora < prazo_limite

    class Meta:
        ordering = ['-data_hora']