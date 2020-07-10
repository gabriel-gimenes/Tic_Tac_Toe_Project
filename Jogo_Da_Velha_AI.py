board = [' ' for x in range(10)]

def insertLetter(letter,pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print(f'{board[1]}|{board[2]}|{board[3]}')
    print(f'{board[4]}|{board[5]}|{board[6]}')
    print(f'{board[7]}|{board[8]}|{board[9]}')

def isWinner(bo,le):
    return ((bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[1] == le and bo[4] == le and bo[7] == le) or
    (bo[2] == le and bo[5] == le and bo[8] == le) or
    (bo[3] == le and bo[6] == le and bo[9] == le) or
    (bo[1] == le and bo[5] == le and bo[9] == le) or
    (bo[3] == le and bo[5] == le and bo[7] == le))

def playerMove(board):
    run = True
    while run:
        move = input('Choose some position[1-8]: ')
        try:
            move = int(move)
            if move >= 1 and move <= 9:
                if spaceIsFree(move):
                    insertLetter('x',move)
                    run = False
                else:
                    print('Sorry...This space is occupied!')
            else:
                print('Please type a valid number!')

        except:
            print("Please type a number!")

def computerMove():
    possibleMoves = [x for x,letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in['o','x']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy,let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move
    
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move

def selectRandom(lista):
    import random
    ln = len(lista)
    r = random.randrange(0,ln)
    return lista[r]

def isBoardFull(board):
    return not(board.count(' ') > 1)

def main():
    draw = False
    print('Welcome to Tic Tac Toe!')
    printBoard(board)
    while not(isBoardFull(board)):
        if not(isWinner(board,'o')):
            playerMove(board)
            printBoard(board)
        else:
            print('The computer won!')
            break

        if not(isWinner(board,'x')):
            move = computerMove()
            if move == 0:
                print('Tie Game!')
                draw = True
            else:
                insertLetter('o',move)
                print(f'Computer placed  an "o" in position {move}')
                printBoard(board)
        else:
            print('The player won!')
            break
    if isBoardFull(board) and not(draw):
        print('Tie Game!')
    
while True:
    main()
    decision = input('Play again?["y" or "n"]: ')
    if decision == 'n':
        break
    else:
        board = [' ' for x in range(10)]