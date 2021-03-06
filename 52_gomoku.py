# 1行5列の五目並べの盤面が与えられます。

# 盤面の各マスには、"O"か"X"か"."が書かれています。

# "O"と"X"は、それぞれプレイヤーの記号を表します。

# 同じ記号が横に連続で5つ並んでいれば、その記号のプレイヤーが勝者となります。

# 勝者の記号を1行で表示してください。
# 勝者がいない場合は、引き分けとして、"D"を表示してください。

#O OOOOO
#X XXXXX
#D .....

masu = input()
if masu == "OOOOO":
    print("O")
elif masu == "XXXXX":
    print("X")
else:
    print("D")

# 正解
#! /usr/local/bin/python3

board = input()
result = 'D'

pivot = board[0]
count = 0
for stone in board:
    if stone != '.' and stone == pivot:
        count += 1
    else:
        break

if count == 5:
    result = pivot

print(result)