# P.43
# 問題文では「男女の数が異なってしまう」「男女が同数」と書いている。
# が、回答のソースコードからは、「男性は男性で同数、女性は女性で同数」ではない場合を求めていることが読み取れる。

from itertools import product

if __name__ == '__main__':
    boy, girl = 20 + 1, 10 + 1
    array = [0] * boy * girl
    array[0] = 1
    for g, b in product(range(girl), range(boy)):
        if b != g and boy - b != girl - g:
            array[b + boy * g] += array[b - 1 + boy * g] if b > 0 else 0
            array[b + boy * g] += array[b + boy * (g - 1)] if g > 0 else 0

    print(array[-2] + array[-boy - 1])
