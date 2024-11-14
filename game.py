from tabnanny import check

from gameparts import TicTacToe

from gameparts import TicTacToe
from gameparts.exceptions import InvalidFieldError, NotEmptyFieldError
import pygame_test

def main():
    tic = TicTacToe()
    current_player = 'X'
    running = True
    pygame_test.pygame.init()
    pygame_test.draw_lines()

    while running:
        for event in pygame_test.pygame.event.get():
            if event.type == pygame_test.pygame.QUIT:
                running = False

            if event.type == pygame_test.pygame.MOUSEBUTTONDOWN:
                mouse_y = event.pos[0]
                mouse_x = event.pos[1]

                clicked_row = mouse_x // pygame_test.CELL_SIZE
                clicked_col = mouse_y // pygame_test.CELL_SIZE

                if tic.board[clicked_row][clicked_col] == ' ':
                    tic.make_move(clicked_row, clicked_col, current_player)
                    current_player = 'O' if current_player == 'X' else 'X'

            if tic.is_board_full():
                rs = 'Ничья\n'
                print(rs)
                save_result(rs)
                running = False

            if tic.check_win():
                rs = f'Победу одержал {current_player}-ик.'
                print(rs)
                save_result(f'Победили {current_player}\n')
                running = False

            pygame_test.draw_figures(tic.board)
        pygame_test.pygame.display.update()

    pygame_test.pygame.quit()

        #print(f'У {current_player}-ка есть шанс изменить ситуацию на поле')

        #while True:
            #try:
                #row = int(input('Введите номер строки: '))
                #column = int(input('Введите номер столбца: '))

                #if row < 0 or row >= tic._field_size:
                    #raise InvalidFieldError
                #if column < 0 or column >= tic._field_size:
                    #raise InvalidFieldError
                #if tic.board[row][column] != ' ':
                    #raise NotEmptyFieldError
            #except NotEmptyFieldError as E:
                #print(E)
                #print('Введите другую ячейку')
                #continue
            #except InvalidFieldError:
                #print(f'Выбирете значения удовл требованию:'
                      #f' 0 <= значение <= {tic._field_size}')
                #continue
            #except ValueError:
                #print('Буквы вводить нельзя. Только числа.')
                #print('Пожалуйста, введите значения для строки и столбца заново.')
                #continue
            #except Exception as E:
                #print(f'Возникла ошибка {E}')
            #else:
                #break




def save_result(result: str):
    with open ('results.txt', 'a', encoding='utf-8') as file:
        file.write(result)

if __name__ == '__main__':
    main()
    print(TicTacToe.__doc__)