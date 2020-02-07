# 正解 15minute
alpha = []
[alpha.append(chr(i)) for i in range(65, 65+26)]

inp = input()

index0 = alpha.index(inp[0])
index1 = alpha.index(inp[-1]) + 1

alpha = alpha[index0:index1]
for i in alpha:
    print(i)

## 解答
#! /usr/local/bin/python3

string = input()
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

first = string[0]
last = string[len(string) - 1]

flag = False
for alphabet in alphabets:
    if first == alphabet:
        flag = True

    if flag:
        print(alphabet)

    if last == alphabet:
        break