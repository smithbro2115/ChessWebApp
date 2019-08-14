from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'chess/home.html')


def move_piece(request):
    if request.method == 'POST':
        print(request.POST['newPos'])
        if 'newPos' in request.POST:
            newPos = request.POST['newPos']
            # doSomething with pieFact here...
            return HttpResponse('success')  # if everything is OK
        # nothing went well
    return HttpResponse('FAIL!!!!!')
