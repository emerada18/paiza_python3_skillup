# あなたは友達たちと N 人でしりとりを行うことにしました。
# 1 人目、 2 人目、...、 N 人目、 1 人目、2 人目、... という順序で発言をします。

# ここで、それぞれの人は、次に挙げる 4 つのしりとりのルールを守って発言をする必要があります。

# 1. 発言は、単語リストにある K 個の単語のうちのいずれかの単語でなければならない。
# 2. 最初の人以外の発言の頭文字は、直前の人の発言の最後の文字と一緒でなければならない。
# 3. 今までに発言された単語を発言してはならない。
# 4. z で終わる単語を発言してはならない。

# ここで、発言の途中で上のルールを破った場合、ルールを破った人はしりとりから外れます。
# そして、その人を抜いて引き続きしりとりを続けていきます。このとき、後続の人は、ルール 2 を守る必要はありません。

# N 人がしりとりを行ったログが M 行分与えられます。
# このとき、M 回の発言が終わった後、しりとりから脱落せずに残っている人のリストを表示するプログラムを書いてくださ

#途中

data = input().split()
ninzu = int(data[0])
tangosu = int(data[2])
log = int(data[2])

tangolist = []
first = True
for i in range(log):
    tango = input()
    if first:
        tangolist.append(tango)
        first = False:

    else:
        if len(tangolist) < tangosu:
            if tango not in tangolist:

                if tango[0] == tangolist[-1][-1]:
                    tangolist.append(tango)

                elif tango[-1] == "z":
                    ninzu -= 1

            elif tango in tangolist:
                ninzu -= 1
    