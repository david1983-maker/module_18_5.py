from django.shortcuts import render


# Create your views here.
def cart(request):
    text = 'Корзина'
    text2 = 'Извините, ваша корзина пуста'
    context = {
        'text': text,
        'text2': text2
    }
    return render(request, 'cart.html',context)


def game(request):
    text = 'ИГРЫ'
    list = ['God of War',
            'Ghost of Tsushima: Director cut',
            'Batman Arkham City']
    context = {
        'text': text,
        'games': list
    }
    return render(request, 'game.html', context)


def platform(request):
    text = 'Главная страница'
    context = {
        'text': text

    }
    return render(request, 'platform.html', context)



