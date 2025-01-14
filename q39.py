# P.163

from itertools import product

if __name__ == '__main__':
    mask = [0] * 16
    for row, col in product(range(4), range(4)):
        mask[row * 4 + col] = (0b1111 << (row * 4)) | (0b1000100010001 << col)

    max_ = 0
    steps = [-1] * (1 << 16)
    steps[0] = 0
    scanner = [0]
    while len(scanner):
        check = scanner.pop(0)
        next_steps = steps[check] + 1
        for i in range(16):
            n = check ^ mask[i]
            if steps[n] == -1:
                steps[n] = next_steps
                scanner.append(n)
                if max_ < next_steps:
                    max_ = next_steps

    print(max_)
    print(bin(steps[max_]))
    selected = [i for i in steps if i == -1]
    print(selected)
