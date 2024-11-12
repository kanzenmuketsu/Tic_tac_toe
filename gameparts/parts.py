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
        for i in range(self._field_size):
            if self.board[i][0] != ' ' and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return  True

        for j in range(self._field_size):
            if self.board[0][j] != ' ' and self.board[0][j] == self.board[1][j] == self.board[2][j] :
                return  True

        if self.board[1][1] != ' ' and self.board[1][1] == self.board[0][0] == self.board[2][2] or \
            self.board[2][0] != ' ' and self.board[2][0] == self.board[1][1] == self.board[0][2]:
                return True

        return False