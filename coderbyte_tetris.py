
def tetrisMove(strArr):
    GAME_WIDTH = 12
    GAME_HEIGHT = 10

    pieceKey = strArr[0]
    strArr.pop(0)

    pieces = {
        "I": [[1, 1, 1, 1]],

        "J": [[1, 1, 1], [0, 0, 1]],

        "L": [[1, 1, 1], [1, 0, 0]],

        "O": [[1, 1], [1, 1]],

        "S": [[0, 1, 1], [1, 1, 0]],

        "T": [[1, 1, 1], [0, 1, 0]],

        "Z": [[1, 1, 0], [0, 1, 1]]
    }

    # Generate blank game board
    board = []
    row = 0
    while row < GAME_HEIGHT:
        ra = []
        col = 0
        while(col < GAME_WIDTH):
            ra.append(0)
            col = col+1
        board.append(ra)
        row = row +1

    # Fill board to given game state
    for i in range(len(strArr)):
        for j in range(int(strArr[i])):
            board[GAME_HEIGHT -1 - j][i] = 1

    piece = pieces[pieceKey]

    # All 4 rotated versions of our piece
    tryPieces = [piece]

    piece = rotateCCW(piece)
    tryPieces.append(piece)

    piece = rotateCCW(piece)
    tryPieces.append(piece)

    piece = rotateCCW(piece)
    tryPieces.append(piece)

    maxScore = 0

    # Try each rotated piece
    for piece in tryPieces:
        pieceHeight = len(piece)
        pieceWidth = len(piece[0])

        # Evaluate specific piece on every game possibility
        row = 0
        max1 = GAME_HEIGHT - pieceHeight
        while(row <= max1):
            col = 0
            max2 = GAME_WIDTH - pieceWidth
            while(col <=max2):
                if validState(piece, row, col, board) and validBottomState(piece, row, col, board):
                    score = evaluateScore(piece, row, col, pieceHeight, board)
                    if (score > maxScore):
                        maxScore = score
                col+=1
            row = row+1

    return maxScore


# Returns score
def evaluateScore(piece, row, col, pieceHeight, board):
    # Copy piece into game state copy
    copy = list(map(list, board))
    r = 0
    while(r<len(piece)):
        c = 0
        while(c<len(piece[0])):
            if piece[r][c] == 1:
                copy[row + r][col+c]=1
            c+=1
        r+=1

    score = 0
    for row in copy:
        control = 1
        for col in row:
            if col == 0:
                control = 0
        if control:
            score +=1

    return score

# Checks if piece is at the bottom of a valid state
def validBottomState(piece, row, col, board):
    # Find bottom of piece
    c = 0
    max1 = len(piece[0])
    while c < max1:
        r = len(piece) -1
        while r >=0:
            if piece[r][c] ==1:
                # Either at the bottom of the board
                # OR the space on the board directly below us is a piece
                if (row + r + 1 >= len(board)) or (board[row + r + 1][col + c] == 1):
                    return True
                break
            r=r-1
        c +=1
    return False

    # Checks if the piece in the given location is a valid game state
    # i.e., returns false if the piece would overlap another piece
def validState(piece, row, col, board):
    r = 0
    while(r < len(piece)):
        c = 0
        while(c < len(piece[0])):
            if (board[row + r][col + c] == 1) and (piece[r][c] == 1):
                return False
            c+=1
        r+=1
    return True

# Returns new piece rotated counter-clockwise
def rotateCCW(piece):
    pieceHeight = len(piece)
    pieceWidth = len(piece[0])

    newPiece = []

    # Generate blank new piece
    row = 0
    while(row < pieceWidth):
        ra = []
        col = 0
        while(col < pieceHeight):
            ra.append(0)
            col+=1
        newPiece.append(ra)
        row +=1

    # Fill new piece from old piece data
    row = 0
    while row < pieceWidth:
        col = 0
        while(col<pieceHeight):
            newPiece[row][col] = piece[col][pieceWidth - 1 - row]
            col+=1
        row += 1
    return newPiece

print(tetrisMove( ["I", "2", "4", "3", "4", "5", "2", "0", "2", "2", "3", "3", "3"]))
print(tetrisMove( ["O", "4", "3", "2", "3", "5", "1", "0", "1", "2", "4", "3", "4"]))