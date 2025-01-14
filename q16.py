# P.75

from itertools import combinations

HANI = 500

if __name__ == '__main__':
    anser = []
    for hen_seihoukei in range(HANI // 4 + 1):
        edge = []
        for tate in range(hen_seihoukei):
            edge.append(tate * (2 * hen_seihoukei - tate))
        for a_chouhoukei_menseki, b_chouhoukei_mensaki in combinations(iterable=edge, r=2):
            if a_chouhoukei_menseki + b_chouhoukei_mensaki == hen_seihoukei * hen_seihoukei:
                anser.append(f'1, {b_chouhoukei_mensaki / float(a_chouhoukei_menseki)}, {hen_seihoukei * hen_seihoukei / float(a_chouhoukei_menseki)}')
    anser = list(set(anser))
    print(len(anser))
