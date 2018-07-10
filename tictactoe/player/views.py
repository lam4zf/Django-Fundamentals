from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from gameplay.models import Game

@login_required
def home(request):
    my_games = Game.objects.games_for_user(request.user)
    all_my_games = my_games.active()
    drawed_games = Game.objects.draw()

    return render(request, "player/home.html",
                    {'games': all_my_games,
                    'drawed_games': drawed_games})
