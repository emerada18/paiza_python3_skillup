##解答
inp = int(input())
list1 = []
dict1 = {}
for i in range(inp):
    inp1 = input().split()
    
    if inp1[0] in dict1.keys():
        dict1[inp1[0]] = dict1[inp1[0]] + int(inp1[1])
    else:
        dict1[inp1[0]] = int(inp1[1])

# print(dict1)

list1 = list(dict1.items())

# for k,v in dict1.items():
#     dict2[v] = k
# print(dict2)
            
# sorteddict2 = sorted(dict2)
# print(sorteddict2)


    
class dictionary:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __repr__(self):
        return repr((self.name, self.value))

sortlist1 = sorted(list1, key=lambda dictionary: dictionary[1], reverse=True)
dict2 = dict(sortlist1)
for k,v in dict2.items():
    print(k,v)


#正解

#! /usr/local/bin/python3

num = int(input())
inputs = {}
result = {}

for i in range(num):
    tmp = input().split()

    exist = False
    for (key, value) in inputs.items():
        if key == tmp[0]:
            exist = True

    if exist:
        inputs[tmp[0]] = inputs[tmp[0]] + int(tmp[1])
    else:
        inputs[tmp[0]] = int(tmp[1])

# ソート用にkeyとvalueを反転させた辞書を作る
for (key, value) in inputs.items():
    result[value] = key

result = sorted(result.items(), reverse=True)

for i in result:
    print(i[1] + ' ' + str(i[0]))