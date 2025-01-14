# P.99

NINZUU = 16

if __name__ == '__main__':
    pair = [0] * (NINZUU // 2 + 1)
    pair[0] = 1
    for index_1 in range(1, NINZUU // 2 + 1):
        for index_2 in range(index_1):
            pair[index_1] += pair[index_2] * pair[index_1 - index_2 - 1]

    print(pair[NINZUU // 2])
