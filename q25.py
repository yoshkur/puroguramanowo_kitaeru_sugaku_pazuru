# P.105

from itertools import permutations, product


KATAGAWA_NO_ANA_NO_KAZU = 6


if __name__ == '__main__':
    max_count = 0
    for hidari_jun, migi_jun in product(permutations(range(1, KATAGAWA_NO_ANA_NO_KAZU)), permutations(range(1, KATAGAWA_NO_ANA_NO_KAZU))):
        path = []
        left = 0
        right = migi_jun[0]
        for i in range(KATAGAWA_NO_ANA_NO_KAZU - 1):
            path.append((left, right))
            left = hidari_jun[i]
            path.append((left, right))
            # 解答でi + 1となっている。インデックスが範囲外になる。
            # rubyだとエラーにならないが、Pythonだとエラーになる。
            # インデックスの範囲内だけ実行する。
            if i < KATAGAWA_NO_ANA_NO_KAZU - 2:
                right = migi_jun[i + 1]
        path.append((left, 0))

        count = 0
        for i in range(KATAGAWA_NO_ANA_NO_KAZU * 2 - 1):
            for j in range(i + 1, KATAGAWA_NO_ANA_NO_KAZU * 2 - 1):
                if (path[i][0] - path[j][0]) * (path[i][1] - path[j][1]) < 0:
                    count += 1
        max_count = max(max_count, count)

    print(max_count)
