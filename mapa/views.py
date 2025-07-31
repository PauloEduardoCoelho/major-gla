from django.shortcuts import render, get_object_or_404
from .models import Ilha, Informacao

def lista_ilhas(request):
    ilhas = Ilha.objects.all()
    return render(request, 'mapa/lista_ilhas.html', {'ilhas': ilhas})

def detalhe_ilha(request, ilha_id):
    ilha = get_object_or_404(Ilha, pk=ilha_id)
    localizacoes = ilha.localizacoes.all().order_by('categoria')
    categorias = {
        'boss': 'Bosses',
        'bau': 'Baús',
        'mob': 'Mobs',
        'quest': 'Quests',
        'achievement': 'Achievements'
    }
    return render(request, 'mapa/detalhe_ilha.html', {
        'ilha': ilha,
        'localizacoes': localizacoes,
        'categorias': categorias
    })

def detalhe_ilha_categoria(request, ilha_id, categoria):
    ilha = get_object_or_404(Ilha, pk=ilha_id)
    localizacoes = ilha.localizacoes.filter(categoria=categoria).order_by('id')

    categorias = {
        'boss': 'Bosses',
        'bau': 'Baús',
        'mob': 'Mobs',
        'quest': 'Quests',
        'achievement': 'Achievements'
    }

    nome_categoria = categorias.get(categoria, 'Desconhecido')

    return render(request, 'mapa/detalhe_ilha_categoria.html', {
        'ilha': ilha,
        'localizacoes': localizacoes,
        'categoria': categoria,
        'nome_categoria': nome_categoria,
    })

def planilha_view(request):
    return render(request, 'mapa/planilha.html')