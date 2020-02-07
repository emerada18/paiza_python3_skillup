# 最初に「ユーザー」 U が1つ与えられます。
# 続いて n 人の「ユーザー」と「ユーザーに対応する血液型」が与えられます。
# 続いて m 種類の「血液型」と「血液型に対応する占い結果」が与えられます。

# 与えられたユーザー U に対応する占い結果を表示してください。

# 入力例の1つ目は、ユーザーの血液型についてのラッキーカラーの占いです。

# 入力例の2つ目は、ユーザーの星座についてのラッキーパーソンの占いになっています。
# 「血液型」として「星座」などのさまざまな文字列を利用できるようにすることで、他の占いにも対応する必要があることに注意してください。


# Kyoko
# 5
# Kyoko B
# Rio O
# Tsubame AB
# KurodaSensei A
# NekoSensei A
# 4
# A red
# B green
# O blue
# AB yellow


user = input()
num_u = int(input())
num_u_list = []
num_u_dict = {}
num_u_dict_blood = {}

for i in range(num_u):
    num_u_list.append(input().split())
print(num_u_list)
    
    # num_u_dict_blood[num_u_list[1]] = num_u_list[0]
    # print(num_u_dict_blood)
    
    # num_u_dict = dict(num_u_list)
    # print(num_u_dict)
    
