<div align="center">

# Leila Hair

### Sistema de Gestão de Agendamentos para Salão de Beleza

*Organizando horários. Controlando faturamento. Simplificando a gestão.*

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap_5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

</div>

---

## 📌 Sobre o Projeto

**Leila Hair** é um sistema desenvolvido para modernizar a gestão de agendamentos do salão de beleza, oferecendo controle total de horários, serviços prestados e uma visão gerencial do faturamento, substituindo processos manuais por uma interface digital elegante e intuitiva.

> **Contexto:** Solução desenvolvida como resposta ao desafio técnico proposto pela empresa **DSIN Tecnologia da Informação**.

---

## Arquitetura e Estrutura de Pastas

O projeto adota uma **arquitetura monolítica** baseada no padrão MVT (Model-View-Template) do Django, com renderização server-side e estilização customizada via Bootstrap.

```
cabeleireira-leila/
│
├── core/                          # 🔵 App principal — Lógica de Negócio
│   ├── migrations/                # Versionamento do esquema do BD
│   ├── templates/
│   │   └── core/
│   │       ├── historico.html         # Listagem e histórico de agendamentos
│   │       ├── form_agendamento.html  # Cadastro e edição
│   │       └── dashboard.html         # Painel gerencial
│   ├── models.py                  # Agendamento, Cliente, Servico
│   ├── views.py                   # Lógica de CRUD e regras de negócio
│   ├── forms.py                   # Formulários e validações
│   └── urls.py                    # Rotas do app
│
├── static/                        # 🟠 Arquivos estáticos
│   ├── css/                        # Estilização customizada
│   └── js/                         # Scripts e interações
│
├── leila_hair/                    # Configurações do projeto Django
│   ├── settings.py
│   └── urls.py
│
├── db.sqlite3
└── manage.py
```

---

## Status de Desenvolvimento

### Back-end — Python + Django + SQLite

| Funcionalidade | Status |
|---|---|
| Modelagem de dados (Agendamento, Cliente, Serviço) | ✅ Concluído |
| CRUD completo de agendamentos | ✅ Concluído |
| Sistema de status (Pendente, Confirmado, Cancelado) | ✅ Concluído |
| Cálculo de faturamento em tempo real | ✅ Concluído |
| Filtros por período de busca | ✅ Concluído |
| Sugestão automática de agrupamento de serviços | ✅ Concluído |
| Travas de segurança contra exclusões acidentais | ✅ Concluído |

### Front-end — HTML5 + CSS3 + Bootstrap 5

| Funcionalidade | Status |
|---|---|
| Layout responsivo com Bootstrap 5 | ✅ Concluído |
| Identidade visual customizada (Custom Design) | ✅ Concluído |
| Ícones via Font Awesome 6 | ✅ Concluído |
| Tela de histórico de agendamentos | ✅ Concluído |
| Painel gerencial (Dashboard) com faturamento | ✅ Concluído |
| Formulários de cadastro e edição | ✅ Concluído |

---

## Destaques Técnicos

### Inteligência de Agendamento
O sistema verifica automaticamente se a cliente já possui outro serviço agendado para a mesma semana e sugere o agrupamento dos atendimentos na mesma data, otimizando a rotina do salão e reduzindo deslocamentos desnecessários.

### Painel Gerencial em Tempo Real
O dashboard calcula dinamicamente o faturamento confirmado e o total de serviços realizados, consultando diretamente os registros com status "Confirmado" no banco de dados, oferecendo uma visão gerencial imediata para a proprietária.

### Sistema de Status Dinâmico
Cada agendamento possui um ciclo de vida (Pendente → Confirmado → Cancelado), com atualização via interface sem necessidade de recarregar a página, garantindo controle de integridade dos registros e prevenindo inconsistências no faturamento.

---

## Roadmap

```
[✅] Modelagem de BD (Agendamento, Cliente, Serviço)
[✅] CRUD completo de agendamentos via Django
[✅] Sistema de status com atualização dinâmica
[✅] Painel gerencial com faturamento em tempo real
[✅] Filtros inteligentes por período
[✅] Sugestão automática de agrupamento de serviços
[✅] Travas de segurança para exclusões
[ ] Autenticação de usuários e controle de acesso
[ ] Deploy em nuvem
```

---

## ▶️ Como Executar Localmente

Siga os passos abaixo para rodar o projeto completo em ambiente de desenvolvimento.

### Pré-requisitos

Certifique-se de ter instalado:

- [Python 3.10+](https://www.python.org/)
- [Git](https://git-scm.com/)

---

### 1. Clone o repositório

```bash
git clone https://github.com/043Cecilio/cabeleireira-leila.git
cd cabeleireira-leila
```

---

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
```

No Windows:
```bash
.\venv\Scripts\activate
```

No Mac / Linux:
```bash
source venv/bin/activate
```

---

### 3. Instale as dependências

```bash
pip install django
```

---

### 4. Execute as migrações do banco de dados

```bash
python manage.py migrate
```

---

### 5. Inicie o servidor

```bash
python manage.py runserver
```

---

### 6. Acesse a aplicação

Com o servidor rodando, acesse:

```
http://127.0.0.1:8000/agendamentos/historico/
```

---

## Stack Tecnológica

| Camada | Tecnologia |
|---|---|
| Linguagem Back-end | Python 3.10+ |
| Framework Back-end | Django |
| Banco de Dados | SQLite |
| Linguagem Front-end | HTML5 + JavaScript |
| Estilização | CSS3 (Custom Design) + Bootstrap 5 |
| Ícones | Font Awesome 6 |
| Versionamento | Git + GitHub |


<div align="center">

Desenvolvido por **Gabriel Cecilio Menezes**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/gabriel-cecilio-bb938035b)

</div>
