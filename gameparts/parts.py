class TicTacToe:
    """
    Класс, который описывает игровое поле для игры
    крестики нолики.
    """
    _field_size = 3
    _CROSS = 'X'
    _ZERO = 'O'

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def __str__(self):
        return (
            'Размер игрового поля -  '
            f'{self.field_size}x{self.field_size}'
        )

    def is_board_full(self) -> bool:
        for row in self.board:
            for place in row:
                if place == " ":
                    return False
        else:
            return True

    def check_win(self):
        for row in self.board:
            pass