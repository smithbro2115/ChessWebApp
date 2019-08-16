from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from chess_web_app.chess.chess_engine.main import games, Game


def home(request):
    return render(request, 'chess/home.html')


@csrf_exempt
def move_piece(request):
    if request.method == 'POST':
        if 'newPos' in request.POST:
            source = request.POST['source']
            target = request.POST['target']
            game_id = request.POST['game_id']
            print(f"{source}{target}", game_id)
            return HttpResponse('success')
    return HttpResponse('FAIL!!!!!')


@csrf_exempt
def start_game(request):
    if request.method == 'POST':
        if 'game_id' in request.POST:
            game_id = request.POST['game_id']
            game = Game(game_id)
            games[game_id] = game
            return HttpResponse('success')
    return HttpResponse('FAIL!!!!!')
