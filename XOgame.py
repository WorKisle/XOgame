board_size = 3

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def draw_board():
    print('_' * 4 * board_size)
    for i in range(board_size):
        print((' ' * 3 + '|') * 3)
        print('', board[i * board_size], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print(('_' * 3 + '|') * 3)


def game_step(index, char):
    if (index > 9 or index < 1 or board[index - 1] in ('x', 'O')):
        return False

    board[index - 1] = char
    return True



def chek_win():
    win = False
    win_combination =(
         (0, 1, 2,), (3, 4, 5), (6, 7, 8),
         (0, 3, 6), (1, 4, 7), (2, 4, 8),
         (0, 4, 8), (2, 4, 6)
    )
    for pos in win_combination:
        if (board [pos [0]] == board [pos [1]] and board [pos [1]] == board [pos [2]]):
            win = board [pos[0]]
    return win


def start_game():
    current_player = 'X'
    step = 1
    draw_board()
    while (step < 10) and (chek_win() == False):
        index = input('Ходит ' + current_player + '. Для хода введите номер поля:')
        if (game_step(int(index), current_player)):
            print('Удачынй ход')
            if (current_player == 'X'):
                current_player = 'O'
            else:
                current_player = 'X'
            draw_board()

            step += 1
        else:
            print('Не верный номер! Повторите!')
    if (step == 10):
        print('Игра завершилась ничьей!')
    else:
        print('Выйграл ' + chek_win())


print('Эта битва будет легендарной!!!')
start_game()
