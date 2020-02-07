kensakusu = int(input())
kensakulist = []
for i in range(kensakusu):
    tango = input()
    if tango not in kensakulist:
        kensakulist.append(tango)
    else:
        kensakulist.remove(tango)
        kensakulist.insert(0, tango)

for i in kensakulist:
    print(i)
    