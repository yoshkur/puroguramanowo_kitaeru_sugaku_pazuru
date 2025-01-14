# P.151

def next_dice(dice):
    top = dice // (6 ** 5)
    left = dice // (6 ** (5 - top))
    right = dice % (6 ** (5 - top))
    return (right + 1) * (6 ** (top + 1)) - (left + 1)


if __name__ == '__main__':
    count = 0
    for i in range(6 ** 6):
        check = []
        while i not in check:
            check.append(i)
            i = next_dice(dice=i)
        count += 1 if check.index(i) else 0

    print(count)
