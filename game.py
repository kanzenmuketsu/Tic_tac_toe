from operator import truediv

from gameparts import TicTacToe
from gameparts.exceptions import InvalidFieldError, NotEmptyFieldError

def main():
    tic = TicTacToe()
    current_player = 'X'
    running = True

    while running:
        print(f'У {current_player}-ка есть шанс изменить ситуацию на поле')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                column = int(input('Введите номер столбца: '))

                if row < 0 or row >= tic._field_size:
                    raise InvalidFieldError
                if column < 0 or column >= tic._field_size:
                    raise InvalidFieldError
                if tic.board[row][column] != ' ':
                    raise NotEmptyFieldError
            except NotEmptyFieldError as E:
                print(E)
                print('Введите другую ячейку')
                continue
            except InvalidFieldError:
                print(f'Выбирете значения удовл требованию:'  
                      f' 0 <= значение <= {tic._field_size}')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue
            except Exception as E:
                print(f'Возникла ошибка {E}')
            else:
                break

        tic.make_move(row, column, current_player)
        tic.display()

        current_player = 'O' if current_player == 'X' else 'X'

        if tic.is_board_full():
            print('Ничья')
            break





    print('hello')

if __name__ == '__main__':
    main()
    print(TicTacToe.__doc__)