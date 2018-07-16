def start_game():
    while True:
        player1 = (input('Player 1, please select X or O: ')).upper()
        if player1 == 'X' or player1 == 'O':
                player2 = 'X' if player1 == 'O' else 'O'
                return {'player1': player1, 'player2': player2};

def player_input(board, player):
    while True:
        result = int(input(f'{player}, please choose number from 1 to 9: '))
        xy_result = translate_move(result)
        if (1 <= result <= 9 and board[xy_result['x']][xy_result['y']] == ' '):
            return xy_result
        else:
            print('The number that you enter is invalid/occupied')

def check_winner(board, move):
    #horizontal check on the move
    if board[move['x']][0] == board[move['x']][1] == board[move['x']][2]:
        return True

    #vertical check on the move
    if board[0][move['y']] == board[1][move['y']] == board[2][move['y']]:
        return True

    #diagonal check
    if move['x'] == move['y'] and board[0][0] == board[1][1] == board [2][2]:
        return True

    if move['x'] + move['y'] == 2 and board[0][2] == board[1][1] == board[2][0]:
        return True

    return False

def translate_move(move):
    switcher = {
        1: {'x': 0, 'y': 0},
        2: {'x': 0, 'y': 1},
        3: {'x': 0, 'y': 2},
        4: {'x': 1, 'y': 0},
        5: {'x': 1, 'y': 1},
        6: {'x': 1, 'y': 2},
        7: {'x': 2, 'y': 0},
        8: {'x': 2, 'y': 1},
        9: {'x': 2, 'y': 2},
    }
    return switcher[move]

def print_board(board):
    for num in range(1, 10, 3):
        print(f'{num} | {num + 1} | {num + 2}')
    print('Please choose the number according to the layout above')
    for row in board:
        print(f'{row[0]} | {row[1]} | {row[2]}')

def assign_board():
    board = []
    for row in range(3):
        board.append([])
        for col in range(3):
            board[row].append(' ')
    return board

def play():
    board = assign_board()
    players = start_game()
    current_player = players['player1']
    while True:
        print_board(board)
        move = player_input(board, current_player)
        board[move['x']][move['y']] = current_player
        if check_winner(board, move):
            print_board(board)
            print(f'{current_player} has won the game')
            break
        else:
            current_player = players['player2'] if current_player == players['player1'] else players['player1']

if __name__ == '__main__':
    play()
