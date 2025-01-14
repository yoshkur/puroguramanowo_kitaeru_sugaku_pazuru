# P.199

N = 16


def graycode(value):
    digits = []
    while value > 0:
        digits.append(value % N)
        value //= N

    for i in range(len(digits) - 1):
        digits[i] = (digits[i] - digits[i + 1]) % N
    return sum([d * (N ** i) for i, d in enumerate(digits)])


def search(value):
    check = graycode(value=value)
    count = 1
    while check != value:
        check = graycode(value=check)
        count += 1
    return count


print(search(value=0x808080))
print(search(value=0xabcdef))
