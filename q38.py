# P.157

from itertools import permutations, product


SEVEN_SEGMENT_CODE = [0b1111110, 0b0110000, 0b1101101, 0b1111001, 0b0110011,
                      0b1011011, 0b1011111, 0b1110000, 0b1111111, 0b1111011]


if __name__ == '__main__':
    flip = [[0] * 10 for _ in range(10)]
    for i, j in product(range(10), range(10)):
        flip[i][j] = str(bin(SEVEN_SEGMENT_CODE[i] ^ SEVEN_SEGMENT_CODE[j]))[2:].count('1')

    min_ = 63
    for seq in permutations(range(10)):
        sum_ = 0
        for j in range(len(seq) - 1):
            sum_ += flip[seq[j]][seq[j + 1]]
            if min_ <= sum_:
                break

        min_ = min(sum_, min_)

    print(min_)
