from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .chess_engine.main import Game, games


def home(request):
    return render(request, 'chess/home.html')


@csrf_exempt
def move_piece(request):
    if request.method == 'POST':
        if 'newPos' in request.POST:
            source = request.POST['source']
            target = request.POST['target']
            game_id = request.POST['game_id']
            data = games[game_id].start_move(source, target)
            return JsonResponse(data)
    return HttpResponse('fail')


@csrf_exempt
def drag_piece(request):
    if request.method == 'POST':
        if 'source' in request.POST:
            source = request.POST['source']
            game_id = request.POST['game_id']
            return HttpResponse(games[game_id].check_if_right_color(source))
    return HttpResponse('fail')


@csrf_exempt
def start_game(request):
    if request.method == 'POST':
        if 'game_id' in request.POST:
            game_id = request.POST['game_id']
            game = Game(game_id)
            games[game_id] = game
            return HttpResponse('success')
    return HttpResponse('fail')
