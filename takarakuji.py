# 今年もパイザ宝くじの季節がやってきました。パイザ宝くじ券には 100000 以上 199999 以下の 6 桁の番号がついています。毎年1つ当選番号 (100000 以上 199999 以下)が発表され、当たりクジの番号が以下のように決まります。

# 1等：当選番号と一致する番号
# 前後賞：当選番号の ±1 の番号（当選番号が 100000 または 199999 の場合，前後賞は一つしかありません）
# 2等：当選番号と下 4 桁が一致する番号（1等に該当する番号を除く）
# 3等：当選番号と下 3 桁が一致する番号（1等および2等に該当する番号を除く）

# たとえば、当選番号が 142358 の場合、当たりの番号は以下のようになります。

# 1等：142358
# 前後賞：142357 と 142359
# 2等：102358, 112358, 122358, …, 192358 （全 9 個）
# 3等：100358, 101358, 102358, …, 199358 （全 90 個）

# あなたが購入した n 枚の宝くじ券の各番号が入力されるので、それぞれの番号について、何等に当選したかを出力するプログラムを書いて下さい。

atari = input()
maisu = int(input())
kuji = []
for i in range(maisu):
    kuji.append(input())

for i in kuji:
    if atari == i:
        print("first")
    elif int(atari) + 1  == int(i) or int(atari) -1 == int(i):
        print("adjacent")
    elif atari[-4:] == i[-4:]:
        print("second")
    elif atari[-3:] == i[-3:]:
        print("third")
    else:
        print("blank")