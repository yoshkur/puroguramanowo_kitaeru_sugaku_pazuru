# P.43
# 問題文では「男女の数が異なってしまう」「男女が同数」と書いている。
# が、回答のソースコードからは、「男性は男性で同数、女性は女性で同数」ではない場合を求めていることが読み取れる。

from itertools import product

if __name__ == '__main__':
    boy, girl = 20 + 1, 10 + 1
    array = [[0] * boy for _ in range(girl)]
    array[0][0] = 1
    for i, j in product(range(girl), range(boy)):
        if j != i and boy - j != girl - i:
            if j > 0:
                array[i][j] += array[i][j - 1]
            if i > 0:
                array[i][j] += array[i - 1][j]

    print(array[girl - 2][boy - 1] + array[girl - 1][boy - 2])
