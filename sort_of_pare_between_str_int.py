# 文字と整数の組のソート (paizaランク C 相当)
# Img 04 03 下記の問題をプログラミングしてみよう！
# 1行目に行数を表す整数 n、続く n 行の各行で「文字」と「整数」の組が空白区切りで入力されます。
# n 個の組を、「整数」の値で昇順に並べ変え、「文字」を出力してください。

# 入力例1
# 2
# A 1
# B 2

# 出力例1
# A
# B

## 正解
#! /usr/local/bin/python3

num = int(input())
inputs = {}

for i in range(num):
    tmp = input().split()
    inputs[int(tmp[1])] = tmp[0]
    # 辞書型の追加

inputs = sorted(inputs.items())
# keyでsort

for i in inputs:
    print(i[1])









## ----------

# # 行数取得
# num = int(input())
# # 変数用意
# setlist = []

# for i in range(num):
#     # range(times)の数だけinput取得
#     input_a = input().split()
#     # listに追加
#     setlist.append(input_a)

# # print(lists)
# # [['G', '0'], ['S', '3'], ['E', '-2']]

# # 辞書型に変換
# dict1 = dict(setlist)
# # to**1 is fail

# # print(dict1)
# # {'G': '0', 'S': '3', 'E': '-2'}

# for i in dict1.keys():
#     to_int = int(i)
#     dict1[1] = to_int
# print(dict1)

## TypeError: list indices must be integers or slices, not str

# list2 = []
# for k, v in dict1.items():
#     list2[v] = k
# print(list2)
# # sortedDict = sorted(dict1, key=lambda x: x[1])
# # print(sortedDict)







# sortedでvalueでsort
# dict2 = sorted(dict1)

# print(dict2)
# ['E', 'G', 'S']
# https://docs.python.org/ja/3/howto/sorting.html

# 配列をひとつずつ取り出す
# for i in dict2:
#     print(i)
## 失敗
# {'H': '-2', 'R': '0', 'W': '-5', 'A': '-1', 'E': '-20'}
# ['A', 'E', 'H', 'R', 'W']
# A
# E
# H
# R
# W





# 原因
# https://note.nkmk.me/python-dict-swap-key-value/

# d_swap = {v: k for k, v in d.items()}
# print(d_swap)

# 共通の値を持っている場合は注意
# 辞書dictのキーkeyはすべて異なる値である必要があるが、値valueは同じ値を保持している可能性がある。

# 共通の値valueを持っている辞書オブジェクトのキーkeyと値valueを入れ替えると、共通の値valueはひとつだけがキーkeyとして残る。

# これは既に存在しているキーkeyを辞書に追加するとその値valueが上書きされてしまうため。

# d_duplicate = {'key1': 'val1', 'key2': 'val1', 'key3': 'val3'}

# d_duplicate_swap = get_swap_dict(d_duplicate)
# print(d_duplicate_swap)
# # {'val1': 'key2', 'val3': 'key3'}


