"""Chess Engine"""
import chess as chess_engine


games = {}


class Game:
    """Chess Game"""
    def __init__(self, game_id):
        self.game_id = game_id
        self.board = chess_engine.Board()

    def start_move(self, source, target):
        move_uci = f"{source}{target}"
        try:
            move = chess_engine.Move.from_uci(move_uci)
            if not self.check_move(move):
                return {'valid': False, 'reason': 'invalid'}
        except ValueError:
            return {'valid': False, 'reason': 'invalid'}
        return {'valid': True, 'fen': self.move(move), 'is_checkmate':
                self.board.is_checkmate(), 'color': self.board.turn}

    def move(self, move):
        self.board.push(move)
        return self.board.fen()

    def check_move(self, move):
        return move in self.board.legal_moves

    def check_if_right_color(self, src):
        src_square = chess_engine.square(convert_letter_to_number(src[0]), int(src[1])-1)
        color_moved = self.board.color_at(src_square)
        if color_moved != self.board.turn:
            return False
        return True


def convert_letter_to_number(letter: str) -> int:
    if letter == 'a':
        return 0
    elif letter == 'b':
        return 1
    elif letter == 'c':
        return 2
    elif letter == 'd':
        return 3
    elif letter == 'e':
        return 4
    elif letter == 'f':
        return 5
    elif letter == 'g':
        return 6
    elif letter == 'h':
        return 7
    elif letter == 'i':
        return 8
    elif letter == 'j':
        return 9
    elif letter == 'k':
        return 10
    elif letter == 'l':
        return 11
    elif letter == 'm':
        return 12
    elif letter == 'n':
        return 13
    elif letter == 'o':
        return 14
    elif letter == 'p':
        return 15
    elif letter == 'q':
        return 16
    elif letter == 'r':
        return 17
    elif letter == 's':
        return 18
    elif letter == 't':
        return 19
    elif letter == 'u':
        return 20
    elif letter == 'v':
        return 21
    elif letter == 'w':
        return 22
    elif letter == 'x':
        return 23
    elif letter == 'y':
        return 24
    elif letter == 'z':
        return 25
