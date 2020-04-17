#Input in the format "bishop a 4" in other words, give the piece name and then the coordinate on the 6x6 chess board one
#piece at a time.

def king_threat(x, y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if arr[x+i][y+j] == "empty":
                arr[x + i][y + j] = "THREAT"


def knight_threat(x,y):
    for i in range(-1, 2, 2):
        for j in range(-1, 2, 2):
            if arr[x+i][y+j*2] == "empty":
                arr[x+i][y+j*2] = "THREAT"
    for i in range(-1, 2, 2):
        for j in range(-1, 2, 2):
            if arr[x+i*2][y+j] == "empty":
                arr[x+i*2][y+j] = "THREAT"


def rook_threat(x, y):
    for j in range(-1, 2, 2):
        positionY = j
        positionX = j
        while arr[x][y+positionY] == "empty" or arr[x][y+positionY] == "THREAT":
            arr[x][y + positionY] = "THREAT"
            positionY += j

        while arr[x+positionX][y] == "empty" or arr[x+positionX][y] == "THREAT":
            arr[x+positionX][y] = "THREAT"
            positionX += j


def bishop_threat(x, y):
    for j in range(-1, 2, 2):
        positionY = j
        positionX = j
        while arr[x + positionX][y + positionY] == "empty" or arr[x + positionX][y + positionY] == "THREAT":
            arr[x + positionX][y + positionY] = "THREAT"
            positionY += j
            positionX += j

        positionY = j
        positionX = j
        while arr[x + positionX][y - positionY] == "empty" or arr[x + positionX][y - positionY] == "THREAT":
            arr[x + positionX][y - positionY] = "THREAT"
            positionX += j
            positionY += j


def queen_threat(x, y):
    rook_threat(x, y)
    bishop_threat(x, y)


board = {}
boardList = []
info = {}
arr = [["empty" for i in range(10)]for j in range(10)]
for i in range(10):
    arr[i][0] = arr[i][9] = arr[0][i] = arr[9][i] = "stop"
    arr[i][1] = arr[i][8] = arr[1][i] = arr[8][i] = "stop"


for q in range (6):
    print("Please enter Piece and location") #king a 3
    temp = input()
    piece, columnLetter, row = temp.split()
    column = ord(columnLetter)-96
    if arr[int(column)+1][int(row)+1] != "empty":
        print ("You overwrote something")
    arr[int(column)+1][int(row)+1] = piece

for y in range(7, 1, -1):
    for x in range(2, 8):
        if arr[x][y] == "empty":
            pass
        elif arr[x][y] == "THREAT":
            pass
        else:
            exec(arr[x][y]+"_threat("+str(x)+","+str(y)+")")

for y in range(7, 1, -1):
    for x in range(2, 8):
        print(arr[x][y], end="\t")
    print()

for y in range(7, 1, -1):
    for x in range(2, 8):
        if arr[x][y] == "empty":
            x_answer = chr(x-1+96)
            y_answer = y-1
            print(x_answer, y_answer)
