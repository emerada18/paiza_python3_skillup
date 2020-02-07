#失敗
result = "D"
board = []

for k in range(5):
    board.append(input())

for i in range(5):
    count = 0
    pivot = ""

    for j in range(5):
        if i == j:
            stone = board[i][j]
        
            if pivot == "":
                pivot = stone
    
            if pivot != "." and pivot == stone:
                count += 1
            else:
                break
    
            if count == 5:
                result = pivot
                
    for j in range(5):
        if i+j == 4:
            stone = board[i][j]
        
            if pivot == "":
                pivot = stone
    
            if pivot != "." and pivot == stone:
                count += 1
            else:
                break
    
            if count == 5:
                result = pivot

        
print(result)


#正解
#! /usr/local/bin/python3

board = []
result = 'D'
direction = [True, False]

for i in range(5):
    board.append(input())

for reverse in direction:
    pivot = ''
    count = 0

    if reverse:
        j = 0
        j_diff = 1
    else:
        j = 4
        j_diff = -1

    for i in range(5):

        stone = board[i][j]

        if pivot == '':
            pivot = stone

        if stone != '.' and stone == pivot:
            count += 1

        j = j + j_diff

    if count == 5:
        result = pivot
        break

print(result)