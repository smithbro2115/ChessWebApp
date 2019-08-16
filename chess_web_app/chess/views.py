from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from chess_engine import main


def home(request):
    return render(request, 'chess/home.html')


@csrf_exempt
def move_piece(request):
    if request.method == 'POST':
        if 'newPos' in request.POST:
            source = request.POST['source']
            target = request.POST['target']
            print(f"{source}{target}")
            return HttpResponse('success')
    return HttpResponse('FAIL!!!!!')
