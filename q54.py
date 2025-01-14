# P.223

N = 11


def search(cards: list, num: int):
    global count
    if num == N + 1:
        count += 1
    else:
        for i in range(2 * N - 1 - num):
            if cards[i] == 0 and cards[i + num + 1] == 0:
                cards[i] = cards[i + num + 1] = num
                search(cards=cards, num=num + 1)
                cards[i] = cards[i + num + 1] = 0


if __name__ == '__main__':
    cards = [0] * N * 2
    count = 0
    search(cards=cards, num=1)
    print(count)
