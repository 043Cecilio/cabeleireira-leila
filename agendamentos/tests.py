from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from .models import Agendamento

class AgendamentoModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_bloqueio_alteracao_menos_de_dois_dias(self):
        """Agendamentos com menos de 2 dias não podem ser alterados pelo sistema"""
        data_proxima = timezone.now() + timedelta(hours=24)
        agendamento = Agendamento.objects.create(
            cliente=self.user, 
            data_hora=data_proxima, 
            status='pendente'
        )
        self.assertFalse(agendamento.pode_alterar_pelo_sistema)

    def test_permissao_alteracao_mais_de_dois_dias(self):
        """Agendamentos com mais de 2 dias podem ser alterados pelo sistema"""
        data_longe = timezone.now() + timedelta(days=5)
        agendamento = Agendamento.objects.create(
            cliente=self.user, 
            data_hora=data_longe, 
            status='pendente'
        )
        self.assertTrue(agendamento.pode_alterar_pelo_sistema)