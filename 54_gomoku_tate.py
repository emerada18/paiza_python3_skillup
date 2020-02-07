result = "D"
board = []

for k in range(5):
    board.append(input())

for i in range(5):
    count = 0
    pivot = ""

    for j in range(5):
        stone = board[j][i]
        
        if pivot == "":
            pivot = stone

        if pivot != "." and pivot == stone:
            count += 1
        else:
            break
    
    if count == 5:
        result = pivot
        break
print(result)
