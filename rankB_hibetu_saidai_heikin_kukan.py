inp1 = input().split()
inp2 = input().split()
list1 = []
list2 = []
dict1 = {}

for i in inp1:
    list1.append(int(i))
    
for i in inp2:
    list2.append(int(i))

for i in range(list1[0]-list1[1]+1):
    key = 0
    value = 0
    for j in range(list1[1]):
        key += list2[i+j]
    dict1[i+1] = key

    
max_k_list = [kv[0] for kv in dict1.items() if kv[1] == max(dict1.values())]
print(str(len(max_k_list)) + " " + str(max_k_list[0]))