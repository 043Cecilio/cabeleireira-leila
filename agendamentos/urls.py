from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.novo_agendamento, name='novo_agendamento'),
    path('historico/', views.historico_agendamentos, name='historico_agendamentos'),
    path('excluir/<int:pk>/', views.excluir_agendamento, name='excluir_agendamento'),
    path('atualizar-status/<int:pk>/', views.atualizar_status, name='atualizar_status'),
    path('alterar/<int:pk>/', views.alterar_agendamento, name='alterar_agendamento'),
]