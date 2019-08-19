from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='chess-app-home'),
    path('move_piece/', views.move_piece, name='chess-app-move-piece'),
    path('drag_piece/', views.drag_piece, name='chess-app-drag-piece'),
    path('start_game/', views.start_game, name='chess-app-start-game')
]
