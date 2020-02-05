##解答
count = int(input())
string = []
for i in range(count):
    string.append(input().split(" "))
print(string)
    
for i in range(count):
    print(string[i][1])
    
##正解
#! /usr/local/bin/python3

num = int(input())

for i in range(num):
    print(input().split()[1])