# P.175

from itertools import product


ENZANSHI = ['+', '-', '*', '//', '']
ANSER = 1234


def repeated_permutation(dimension: int, iterable) -> list:
    return product(iterable, repeat=dimension)


if __name__ == '__main__':
    found = False
    dimension = 1
    while not found:
        for o in repeated_permutation(dimension=dimension, iterable=ENZANSHI):
            for i in range(1, 10):
                expr = str(i)
                for op in o:
                    expr += op + str(i)
                if eval(expr) == ANSER:
                    print(expr.replace('//', '/'))
                    found = True
        dimension += 1
