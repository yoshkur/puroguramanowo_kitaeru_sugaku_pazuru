# P.91

MAGIC_SQUARE = [1, 14, 14, 4, 11, 7, 6, 9, 8, 10, 10, 5, 13, 2, 3, 15]
SUM_ALL = sum(MAGIC_SQUARE)


if __name__ == '__main__':
    sum_ = [0] * (SUM_ALL + 1)
    sum_[0] = 1
    for number in MAGIC_SQUARE:
        for index in range(SUM_ALL - number + 1, 0, -1):
            sum_[index - 1 + number] += sum_[index - 1]

    print(sum_.index(max(sum_)))
