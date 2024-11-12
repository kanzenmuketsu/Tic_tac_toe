from operator import truediv

from gameparts import TicTacToe
from gameparts.exceptions import InvalidFieldError

def main():
    tic = TicTacToe()


    while True:
        try:
            row = int(input('Введите номер строки: '))
            column = int(input('Введите номер столбца: '))

            if row < 0 or row >= tic._field_size:
                raise InvalidFieldError
            if column < 0 or column >= tic._field_size:
                raise InvalidFieldError
        except InvalidFieldError:
            print(f'Выбирете значения удовл требованию:'
                  f' 0 <= значение <= {tic._field_size}')
            continue
        except ValueError:
            print('Буквы вводить нельзя. Только числа.')
            print('Пожалуйста, введите значения для строки и столбца заново.')
        else:
            break

    tic.make_move(row, column, TicTacToe._ZERO)
    tic.display()

    print('hello')

if __name__ == '__main__':
    main()
    print(TicTacToe.__doc__)