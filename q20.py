# P.91

from itertools import combinations


MAGIC_SQUARE = [1, 14, 14, 4, 11, 7, 6, 9, 8, 10, 10, 5, 13, 2, 3, 15]

if __name__ == '__main__':
    sum_ = {}
    for index in range(len(MAGIC_SQUARE)):
        for set_ in combinations(MAGIC_SQUARE, index + 1):
            key = sum(set_)
            sum_[key] = sum_.get(key, 0) + 1

    sorted_sum = sorted(sum_.items(), key=lambda x: x[1])
    print(sorted_sum[-1][0])
