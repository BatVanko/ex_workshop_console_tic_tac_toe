def print_board_numeration(board_size):
    index = 1
    for i in range(board_len):
        print('|', end='')
        for _ in range(board_len):
            print(f"  {index}  |", end='')
            index += 1
        print()


def number_positions(board_l):
    num_positions = dict()
    idx = 1
    for i in range(board_l):
        for j in range(board_l):
            num_positions[idx] = (i, j)
            idx += 1
    return num_positions


def print_game_board(matrix):
    for i in range(len(matrix)):
        print('|', end='')
        for j in range(len(matrix)):
            if matrix[i][j] is not None:
                print(f"  {matrix[i][j]}  |", end='')
            else:
                print(f"  {' '}  |", end='')

        print()


def check_win_position(cur_row, cur_col, first_name, second_name, first_p_sign, second_p_sign, field):
    is_full = True
    main_diagonal_counter_player1 = 0
    main_diagonal_counter_player2 = 0
    second_diagonal_counter_player1 = 0
    second_diagonal_counter_player2 = 0
    max_equal_positions = len(field)
    for r in range(len(field)):
        for c in range(len(field)):
            if board[r][c] is None:
                is_full = False
            if r == c:
                if field[r][c] == first_p_sign:
                    main_diagonal_counter_player1 += 1
                elif field[r][c] == second_p_sign:
                    main_diagonal_counter_player2 += 1
            if r == len(field) - 1 - c:
                if field[r][c] == first_p_sign:
                    second_diagonal_counter_player1 += 1
                elif field[r][c] == second_p_sign:
                    second_diagonal_counter_player2 += 1
            if main_diagonal_counter_player1 == max_equal_positions or main_diagonal_counter_player2 == max_equal_positions or second_diagonal_counter_player1 == max_equal_positions:
                break
    row_win_1 = True
    row_win_2 = True
    for c_col in range(len(field)):
        if field[cur_row][c_col] != first_p_sign:
            row_win_1 = False
        if field[cur_row][c_col] != second_p_sign:
            row_win_2 = False
    col_win_1 = True
    col_win_2 = True
    for c_row in range(len(field)):
        if field[c_row][cur_col] != first_p_sign:
            col_win_1 = False
        if field[c_row][cur_col] != second_p_sign:
            col_win_2 = False

    if row_win_1 or col_win_1 or main_diagonal_counter_player1 == max_equal_positions or second_diagonal_counter_player1 == max_equal_positions:
        return f'{first_name} won!'
    if row_win_2 or col_win_2 or main_diagonal_counter_player2 == max_equal_positions or second_diagonal_counter_player2 == max_equal_positions:
        return f'{second_name} won!'
    if is_full:
        return 'The game ends in a draw!'


player_one_name = input('Player one name: ')
player_two_name = input('Player two name: ')
player_one_symbol = input(f"{player_one_name} would you like to play with 'X' or 'O'").upper()
player_two_symbol = ('X' if player_one_symbol == 'O' else 'O').upper()
board_len = 3
board_max_len = board_len * board_len
print('This is the numeration of the board:')
print_board_numeration(board_len)
board = [[None] * board_len for _ in range(board_len)]
print(f'{player_one_name} starts first!')
numbers_and_positions = number_positions(board_len)
left_border = 1
right_border = board_len * board_len

while True:
    current_player = player_one_name
    move = int(input(f'{player_one_name} choose a free positions [1-{board_max_len}]: '))
    if left_border > move or move > right_border:
        continue
    row, col = numbers_and_positions[move]
    if board[row][col] is not None:
        continue
    current_player_symbol = ''

    if current_player == player_one_name:
        current_player_symbol = player_one_symbol
    else:
        current_player_symbol = player_two_symbol
    board[row][col] = current_player_symbol
    print_game_board(board)
    list_of_won_returns = [f'{player_one_name} won!', f'{player_two_name} won!', 'The game ends in a draw']
    result = check_win_position(row, col, player_one_name, player_two_name, player_one_symbol, player_two_symbol, board)
    if result in list_of_won_returns:
        print(result)
        break

    (player_one_name, player_one_symbol), (player_two_name, player_two_symbol) = (player_two_name, player_two_symbol), (
        player_one_name, player_one_symbol)
