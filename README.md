# VacinaKids

> Sistema web para gestão de vacinação infantil com acompanhamento de carteira de vacinação, lembretes automáticos e registro de doses aplicadas.

![Django](https://img.shields.io/badge/Django-5.2+-092E20?style=flat-square&logo=django)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-336791?style=flat-square&logo=postgresql)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

## 📋 Sobre o Projeto

VacinaKids é uma aplicação web desenvolvida em Django que facilita o gerenciamento completo da carteira de vacinação de crianças. O sistema permite que responsáveis registrem dados dos filhos, acompanhem suas vacinas aplicadas, recebam lembretes automáticos e visualizem relatórios de vacinação.

### Principais Funcionalidades

✅ **Gestão de Crianças** - Registre e mantenha informações básicas das crianças (nome, data de nascimento, CPF, nome da mãe)

✅ **Carteira de Vacinação** - Acompanhe todas as vacinas recomendadas e registre doses aplicadas

✅ **Catálogo de Vacinas** - Banco de dados de vacinas com informações de faixa etária recomendada

✅ **Registro de Doses** - Registre datas de aplicação de cada vacina com histórico completo

✅ **Lembretes Automáticos** - Notificações agendadas para próximas vacinas recomendadas

✅ **Relatórios** - Geração de relatórios de vacinação em PDF

✅ **Autenticação** - Sistema de autenticação via CPF com opção de receber notificações por email

✅ **Painel Administrativo** - Interface Django Admin para gerenciamento completo dos dados

✅ **Interface Responsiva** - Design moderno com Tailwind CSS compatível com dispositivos móveis

## 🚀 Stack Tecnológico

### Backend
- **Django 5.2** - Framework web Python
- **Django REST Framework** - API REST
- **PostgreSQL** - Banco de dados
- **Gunicorn** - Servidor WSGI

### Frontend
- **Tailwind CSS** - Framework CSS utilitário
- **Django Tailwind** - Integração do Tailwind com Django
- **HTML/JavaScript** - Templates dinâmicos

### DevOps & Ferramentas
- **Render** - Hospedagem em produção
- **WhiteNoise** - Servidor de arquivos estáticos
- **django-crontab** - Agendamento de tarefas periódicas
- **dj-database-url** - Configuração de banco de dados
- **python-decouple** - Variáveis de ambiente

## 📦 Instalação

### Pré-requisitos
- Python 3.12+
- PostgreSQL 12+
- pip ou poetry
- Node.js (para compilar Tailwind)

### Passos de Instalação

#### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/VacinaKids.git
cd VacinaKids
```

#### 2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

#### 3. Instale as dependências Python
```bash
pip install -r requirements.txt
```

#### 4. Instale as dependências Node.js
```bash
npm install
```

#### 5. Configure as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto:
```env
DEBUG=True
SECRET_KEY=sua-chave-secreta-super-segura
DATABASE_URL=postgresql://usuario:senha@localhost:5432/vacinakids
ADMIN_CPF=12345678900
ADMIN_PASSWORD=senha_admin_super_segura
```

#### 6. Execute as migrações do banco de dados
```bash
python manage.py migrate
```

#### 7. Crie um superusuário (opcional)
```bash
python manage.py createsuperuser
```

#### 8. Colete arquivos estáticos
```bash
python manage.py collectstatic --noinput
```

## 🏃 Como Executar

### Modo Desenvolvimento
```bash
npm run dev
```
Isto executará simultaneamente:
- Servidor Django em http://localhost:8000
- Compilação automática do Tailwind CSS em modo watch

### Modo Produção
```bash
gunicorn VacinaKids.wsgi --bind 0.0.0.0:8000
```

## 📁 Estrutura do Projeto

```
VacinaKids/
├── accounts/              # Aplicação de autenticação e contas
│   ├── models.py         # Modelo customizado de usuário
│   ├── forms.py          # Formulários de autenticação
│   ├── views.py          # Views de login e configurações
│   └── urls.py           # URLs da aplicação
├── children/             # Gestão de crianças
│   ├── models.py         # Modelo de Criança
│   ├── views.py          # Views CRUD de crianças
│   └── forms.py          # Formulários de crianças
├── vaccines/             # Catálogo de vacinas
│   ├── models.py         # Modelo de Vacina
│   ├── views.py          # Views de vacinas
│   └── forms.py          # Formulários de vacinas
├── records/              # Registro de vacinação
│   ├── models.py         # Modelo de VaccinationRecord
│   ├── views.py          # Views de registros
│   └── forms.py          # Formulários de registros
├── notifications/        # Sistema de notificações
│   ├── models.py         # Modelos de notificação
│   ├── views.py          # Views de notificações
│   └── management/
│       └── commands/
│           └── send_vaccine_reminders.py  # Comando agendado
├── reports/              # Geração de relatórios
│   ├── models.py         # Modelos de relatório
│   ├── views.py          # Views de relatórios
│   └── forms.py          # Formulários de filtros
├── theme/                # Tema customizado e assets
│   ├── static_src/       # Arquivos-fonte (Tailwind)
│   └── templates/        # Templates base
├── templates/            # Templates HTML
├── static/               # Arquivos estáticos (CSS, JS, imagens)
├── staticfiles/          # Arquivos estáticos coletados (produção)
├── VacinaKids/           # Configurações do projeto
│   ├── settings.py       # Configurações do Django
│   ├── urls.py           # URLs principais
│   ├── wsgi.py           # Configuração WSGI
│   └── asgi.py           # Configuração ASGI
├── manage.py             # Script de gerenciamento do Django
├── requirements.txt      # Dependências Python
├── package.json          # Dependências Node.js
├── Procfile              # Configuração para Heroku/Render
└── runtime.txt           # Versão do Python
```

## 🔐 Modelos de Dados

### User
```python
- cpf (CharField, único) - Identificador principal
- first_name, last_name - Nome completo
- email - Email do usuário
- receive_email_notifications - Flag para notificações
- is_active, is_staff - Status do usuário
- date_joined - Data de cadastro
```

### Child
```python
- owner (ForeignKey para User) - Responsável
- name - Nome da criança
- birth_date - Data de nascimento
- mother_name - Nome da mãe
- cpf - CPF (único)
- created_at, updated_at - Timestamps
```

### Vaccine
```python
- name - Nome da vacina
- description - Descrição detalhada
- recommended_age_months - Idade recomendada em meses
- created_at, updated_at - Timestamps
```

### VaccinationRecord
```python
- child (ForeignKey) - Criança vacinada
- vaccine (ForeignKey) - Vacina aplicada
- applied_date - Data de aplicação
- created_at, updated_at - Timestamps
```

## 🔧 Comandos Úteis

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Limpar banco de dados (dev apenas!)
python manage.py migrate zero

# Acesso ao shell Django
python manage.py shell

# Iniciar servidor de desenvolvimento
python manage.py runserver

# Executar testes
python manage.py test

# Compilar assets do Tailwind
python manage.py tailwind build
python manage.py tailwind start  # Mode watch

# Enviar lembretes de vacinação (agendado via cron)
python manage.py send_vaccine_reminders
```

## 📧 Configuração de Notificações

O sistema possui um comando agendado para enviar lembretes de vacinação. Configure no `settings.py`:

```python
CRONJOBS = [
    ('0 9 * * *', 'notifications.management.commands.send_vaccine_reminders.Command'),
]
```

Isto executará diariamente às 09:00 para notificar usuários sobre próximas vacinações.

## 🧪 Testes

```bash
# Executar todos os testes
python manage.py test

# Executar testes de uma aplicação específica
python manage.py test accounts
python manage.py test children
python manage.py test vaccines
python manage.py test records
python manage.py test reports
python manage.py test notifications

# Executar com saída verbosa
python manage.py test --verbosity=2
```

## 🚢 Deploy

### Deploy no Render

1. Faça push do código para um repositório Git (GitHub, GitLab, etc)

2. Conecte seu repositório no Render (render.com)

3. Configure as variáveis de ambiente:
   - `DEBUG=False`
   - `SECRET_KEY` - Chave secreta forte
   - `DATABASE_URL` - URL da conexão PostgreSQL
   - Outras conforme necessário

4. Configure o build command:
   ```
   pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
   ```

5. Configure o start command:
   ```
   gunicorn VacinaKids.wsgi
   ```

6. Deploy será feito automaticamente

## 📝 Variáveis de Ambiente

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| `DEBUG` | Modo debug do Django | False |
| `SECRET_KEY` | Chave secreta do Django | Requerido |
| `DATABASE_URL` | URL de conexão do banco | Requerido |
| `ADMIN_CPF` | CPF do admin inicial | Opcional |
| `ADMIN_PASSWORD` | Senha do admin inicial | Opcional |
| `ALLOWED_HOSTS` | Hosts permitidos | * |

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Diretrizes de Código
- Siga o PEP 8
- Adicione docstrings em funções e classes
- Escreva testes para novas funcionalidades
- Mantenha a compatibilidade com Django 5.2+

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 📞 Suporte

Para reportar bugs ou solicitar funcionalidades, abra uma issue no repositório.

## 👥 Autores

- Desenvolvido com ❤️ para melhorar a saúde infantil

---

**Última atualização**: Março de 2026

*VacinaKids - Cuidando da saúde das crianças através da tecnologia* 💉👶
