#my answer
inp = int(input())
inp2 = []
for i in range(inp):
    inp2.append(input().split())
    
for i in range(inp):
    inp2[i][1] = int(inp2[i][1])

dict_inp2 = dict(inp2)
sorted_dict_inp2 = sorted(dict_inp2.items(), key=lambda x:x[1])

for v in range(inp):
    print(sorted_dict_inp2[v][0])

#! /usr/local/bin/python3
# answer
num = int(input())
inputs = {}

for i in range(num):
    tmp = input().split()
    inputs[int(tmp[1])] = tmp[0]

inputs = sorted(inputs.items())

for i in inputs:
    print(i[1])