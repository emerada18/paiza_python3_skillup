#解答
inp = input()
inp1 = input().split()
int_inp1 = [int(i) for i in inp1]

sortint = sorted(int_inp1)
for i in sortint:
    print(i)


#正解
#! /usr/local/bin/python3

input()  # 1つ目の入力は使わないので読み飛ばす
strings = input().split()
nums = []

for num in strings:
    nums.append(int(num))

nums.sort()

for i in nums:
    print(i)