from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def cart(request):
    return render(request, 'cart.html')


def game(request):
    title = 'ИГРЫ'
    game1 = 'God of War'
    game2 = 'Ghost of Tsushima: Director cut'
    game3 = 'Batman Arkham City'
    context = {
        'title': title,
        'text1': game1,
        'text2': game2,
        'text3': game3
    }
    return render(request, 'game.html',context)


def platform(request):
    text = 'Главная страница'
    context = {
        'text': text

    }
    return render(request, 'platform.html', context)
