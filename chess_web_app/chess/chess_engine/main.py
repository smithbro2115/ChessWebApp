"""Chess Engine"""
import chess


games = {}


class Game:
    """Chess Game"""
    def __init__(self, game_id):
        self.game_id = game_id
        self.board = chess.Board()
