# P.47

EOUROPIAN = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13,
             36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14,
             31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
AMERICAN = [0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 5, 22, 34,
            15, 3, 24, 36, 13, 1, 00, 27, 10, 25, 29, 12, 8,
            19, 31, 18, 6, 21, 33, 16, 4, 23, 35, 14, 2]


def sum_max(roulette: list, renzoku_waku_su: int):
    anser = sum(roulette[0: renzoku_waku_su])
    temp = anser
    for waku_number in range(len(roulette)):
        sentou = (waku_number + renzoku_waku_su) % len(roulette)
        temp += roulette[sentou]
        temp -= roulette[waku_number]
        anser = max(anser, temp)
    return anser


if __name__ == '__main__':
    count = 0
    for i in range(2, 37):
        count += 1 if sum_max(roulette=EOUROPIAN, renzoku_waku_su=i) < sum_max(roulette=AMERICAN, renzoku_waku_su=i) else 0
    print(count)
