# 💼 PJControl

**PJControl** é uma aplicação web desenvolvida para auxiliar **profissionais PJ (Pessoa Jurídica)** no cálculo e controle de custos mensais, considerando despesas fixas, variáveis, tributos e reservas financeiras.

O sistema foi criado para simplificar a gestão financeira de prestadores de serviços, oferecendo um cálculo rápido e preciso do **lucro líquido**, com base nas principais deduções que impactam o resultado final.

---

## 🚀 Demonstração

Acesse o sistema online:  
👉 [https://pjtinha.onrender.com/](https://pjtinha.onrender.com/)

---

## ⚙️ Funcionalidades

- Cálculo automático de:
  - **Pro-labore**
  - **DAS (Simples Nacional)**
  - **INSS**
  - **Custos fixos e variáveis**
  - **Reserva financeira**
- Exibição detalhada do resultado:
  - Base de cálculo
  - Total de despesas
  - Lucro líquido final
- Interface simples, direta e intuitiva

---

## 🧠 Tecnologias Utilizadas

| Categoria | Tecnologia |
|------------|-------------|
| **Linguagem principal** | [Python 3](https://www.python.org/) |
| **Framework web** | [Flask](https://flask.palletsprojects.com/) |
| **Servidor de produção** | [Gunicorn](https://gunicorn.org/) |
| **Hospedagem** | [Render](https://render.com/) |
| **Frontend** | HTML + Jinja2 Templates |

---

## 🧩 Estrutura do Projeto

├── main.py # Arquivo principal da aplicação Flask
├── templates/ # Páginas HTML (interface do usuário)
│ ├── calcular.html
│ └── resultado.html
├── requirements.txt # Dependências do projeto
└── Procfile # Configuração para deploy (Render)  

