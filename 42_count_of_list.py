# 指定された配列（リスト）の定義の中で、同じ要素の数をカウントして、その数を出力してください。

# ▼　下記回答欄にコードを記入してみよう

# 入力される値
# なし

# "HND", "NRT", "KIX", "NGO", "NGO", "NGO", "NGO", "NGO"
# を要素に持つ配列（リスト）をプログラムで定義し、使用すること。
# ただし、2つ以上同じ要素が出現するのは、1種類の文字列についてだけです。



# 解答
airports = ["HND", "NRT", "KIX", "NGO", "NGO", "NGO", "NGO", "NGO"]
counter = 0
for i in airports:
    airports.count(i)
    if counter < airports.count(i):
        counter = airports.count(i)
print(counter)




# 正解
#! /usr/local/bin/python3
array = ["HND", "NRT", "KIX", "NGO", "NGO", "NGO", "NGO", "NGO"]
count = {}

for pattern in array:
    if pattern in count:
        count[pattern] += 1
    else:
        count[pattern] = 1

for (key, value) in count.items():
    if value != 1:
        print(value)