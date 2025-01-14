# P.61

# 処理速度を意識したコード。
# テキスト通りにコーディングしたつもりだが、結果が違う。
from itertools import permutations


if __name__ == '__main__':
    count = 0
    for e, a, d, t, k, l in permutations(range(10), 6):
        if a + t in [8, 9, 10] and a + e in [8, 9, 10] and (d + e + k) % 10 == 1 and ((a + t + l) * 10 + d + e + k) % 100 == l * 11:
            nokori_suji = list(set(range(10)) - set([e, a, d, t, k, l]))
            for i, r, s, w in permutations(nokori_suji):
                if r and w and t and s in [w + 1, w + 2]:
                    read = r * 1000 + e * 100 + a * 10 + d
                    write = w * 10000 + r * 1000 + i * 100 + t * 10 + e
                    talk = t * 1000 + a * 100 + l * 10 + k
                    skill = s * 10000 + k * 1000 + i * 100 + l * 10 + l
                    if read + write + talk == skill:
                        print(f'{read} + {write} + {talk} = {skill}')
                        count += 1
    print(count)
