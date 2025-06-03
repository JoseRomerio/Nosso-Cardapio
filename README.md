# Cardápio Digital

Um aplicativo web desenvolvido em Django para exibição de cardápio digital com categorias e produtos.

## Funcionalidades

- Exibição de produtos organizados por categorias
- Menu lateral para filtro de categorias
- Interface responsiva
- Suporte a imagens dos produtos
- Preços e descrições dos produtos
- Design moderno e intuitivo

## Tecnologias Utilizadas

- Python 3.13.3
- Django 5.2.1
- Bootstrap 5.3.0
- Font Awesome 6.0.0
- Pillow 11.2.1

## Requisitos do Sistema

- Python 3.13 ou superior
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd [NOME_DO_DIRETÓRIO]
```

2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Execute as migrações:
```bash
python manage.py migrate
```

6. Crie um superusuário:
```bash
python manage.py createsuperuser
```

7. Inicie o servidor:
```bash
python manage.py runserver
```

8. Acesse o aplicativo:
- Admin: http://127.0.0.1:8000/admin/
- Cardápio: http://127.0.0.1:8000/

## Estrutura do Projeto

```
cardapio_project/
├── cardapio/
│   ├── migrations/
│   ├── templates/
│   │   └── cardapio/
│   │       └── cardapio.html
│   │
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── cardapio_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/
├── static/
├── manage.py
├── requirements.txt
└── README.md
```

## Uso

1. Acesse o painel administrativo em `/admin`
2. Adicione categorias para seus produtos
3. Adicione produtos com suas respectivas categorias
4. As imagens dos produtos serão salvas na pasta `media/`
5. O cardápio será exibido na página principal

## Contribuição

Desenvolvido por Romério

## Licença

Este projeto está sob a licença MIT. 