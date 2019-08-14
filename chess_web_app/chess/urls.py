from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='chess-home'),
    path('move_piece/', views.move_piece, name='chess-move-piece')
]