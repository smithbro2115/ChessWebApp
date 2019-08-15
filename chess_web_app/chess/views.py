from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'chess/home.html')


@csrf_exempt
def move_piece(request):
    if request.method == 'POST':
        print(request.POST)
        if 'newPos' in request.POST:
            newPos = request.POST['newPos']
            return HttpResponse('success')
    return HttpResponse('FAIL!!!!!')
