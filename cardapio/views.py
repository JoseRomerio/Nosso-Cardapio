from django.shortcuts import render
from .models import Categoria, ItemCardapio

def cardapio(request):
    categorias = Categoria.objects.all()
    itens = ItemCardapio.objects.filter(disponivel=True)
    return render(request, 'cardapio/cardapio.html', {
        'categorias': categorias,
        'itens': itens
    })
