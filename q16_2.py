# P.75

from itertools import combinations
from math import gcd

HANI = 500

if __name__ == '__main__':
    count = 0
    for hen_seihoukei in range(HANI // 4 + 1):
        for a_chouhoukei_menseki, b_chouhoukei_menseki in combinations(iterable=range(hen_seihoukei), r=2):
            if a_chouhoukei_menseki ** 2 + b_chouhoukei_menseki ** 2 == hen_seihoukei * hen_seihoukei:
                if gcd(a_chouhoukei_menseki, b_chouhoukei_menseki) == 1:
                    count += 1
    print(count)
