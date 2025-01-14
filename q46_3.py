# P.191

def count_swap(n: int):
    if n == 1:
        return 0
    result = n - 1
    for i in range(1, n):
        result *= i
    result += n * count_swap(n=n - 1)
    return result


if __name__ == '__main__':
    print(count_swap(n=7))
