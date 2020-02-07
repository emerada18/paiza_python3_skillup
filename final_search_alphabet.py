# # 1行目の英大文字 X から、2行目の英大文字 Y の範囲に3行目のアルファベット C
# が含まれていれば"true", そうでなければ"false"と出力してください。
# # X が Y よりもアルファベット順で後ろになる場合(X = 'G', Y = 'F'のときなど)も
# "false"と出力してください。

# x1 - c3 - y2 : true
## inputx - inputc - inputy
# A - y -x,c : false
# x - y - c : false


##解答
alpha = []
[alpha.append(chr(i)) for i in range(65, 65+26)]

inputx = input()
inputy = input()
inputc = input()

check = ""

for i in alpha:
    if inputx == i:
        checkx = i
    elif inputy == i:
        checky = i
    elif inputc == i:
        checkc = i

index_x = alpha.index(inputx)
index_y = alpha.index(inputy)
index_c = alpha.index(inputc)

if index_x <= index_c and index_c <= index_y:
    print("true")
else:
    print("false")

##正解
#! /usr/local/bin/python3


first = input()
last = input()
pattern = input()

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
result = 'false'

in_a_range = False
for alphabet in alphabets:
    if first == alphabet:
        in_a_range = True

    if in_a_range and pattern == alphabet:
        result = 'true'

    if last == alphabet:
        break

print(result)