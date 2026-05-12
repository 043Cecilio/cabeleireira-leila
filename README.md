💇‍♀️ Sistema de Gestão Cabeleireira Leila


<img width="1920" height="1080" alt="Captura de tela 2026-05-11 235153" src="https://github.com/user-attachments/assets/a9885023-0d13-4c39-8012-796ce6ced271" />
<img width="1920" height="1080" alt="Captura de tela 2026-05-11 235209" src="https://github.com/user-attachments/assets/78f1bbb8-f18d-4468-bf96-72b9248b787b" />


📝 Sobre o Projeto

Este sistema foi desenvolvido para modernizar a gestão de agendamentos do salão Leila Hair. Ele permite o controle total de horários, serviços prestados e oferece uma visão gerencial do faturamento, substituindo processos manuais por uma interface digital elegante e intuitiva, solução do desafio proposto para empresa DSIN Tecnologia da Informação. 

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

Banco de Dados: SQLite.

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
