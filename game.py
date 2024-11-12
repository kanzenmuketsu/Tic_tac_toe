from gameparts import TicTacToe

def main():
    tic = TicTacToe()
    tic.make_move(2, 1, TicTacToe._ZERO)
    tic.display()

    print('hello')

if __name__ == '__main__':
    main()