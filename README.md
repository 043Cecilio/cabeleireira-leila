💇‍♀️ Sistema de Gestão Cabeleireira Leila

📝 Sobre o Projeto

Este sistema foi desenvolvido para modernizar a gestão de agendamentos do salão Leila Hair. Ele permite o controle total de horários, serviços prestados e oferece uma visão gerencial do faturamento, substituindo processos manuais por uma interface digital elegante e intuitiva.

🚀 Funcionalidades Principais

Gestão de Agendamentos: Cadastro, edição, visualização e exclusão de horários.

Painel Gerencial (Dashboard): Visualização em tempo real do faturamento confirmado e total de serviços realizados.

Filtros Inteligentes: Busca de agendamentos por períodos específicos.

Sistema de Status: Controle de atendimentos (Pendente, Confirmado, Cancelado) com atualização dinâmica.

Inteligência de Agendamento: Sugestão automática para agrupar serviços da mesma cliente na mesma data dentro da semana.

Segurança de Dados: Travas de segurança para evitar exclusões acidentais e controle de integridade dos registros.

🛠 Tecnologias Utilizadas
Backend: Python com o framework Django.

Frontend: HTML5, CSS3 (Custom Design), JavaScript e Bootstrap 5.

Ícones: Font Awesome 6.

Banco de Dados: SQLite (em desenvolvimento).

Versionamento: Git e GitHub.

💻 Como Rodar o Projeto
Pré-requisitos
Python 3.10 ou superior instalado.

Git instalado.

Passo a Passo

1 - Clonar o repositório:
    
    git clone https://github.com/043Cecilio/cabeleireira-leila.git
    cd cabeleireira-leila

2 - Criar e ativar o ambiente virtual:

    python -m venv venv
    No Windows: .\venv\Scripts\activate
    No Mac / Linux: source venv/bin/activate

3 - Instalar as dependências:

    pip install django

4 - Executar as migrações do banco de dados:

    python manage.py migrate

5 - Iniciar o servidor:

    python manage.py runserver

6 - ACESSE: 

    http://127.0.0.1:8000/agendamentos/historico/
