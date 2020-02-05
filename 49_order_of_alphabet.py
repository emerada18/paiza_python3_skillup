##解答
string = input()

st0 = string[0]
st1 = string[-1]

for i in range(65, 65+26):
    if chr(i) == st0:
        chr1 = i
    elif chr(i) == st1:
        chr2 = i
    
if chr2 > chr1:
    print("true")
else:
    print("false")

##正解
#! /usr/local/bin/python3

string = input()
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
result = 'true'

first = string[0]
last = string[len(string) - 1]

for alphabet in alphabets:
    if first == alphabet:
        break

    if last == alphabet:
        result = 'false'

print(result)