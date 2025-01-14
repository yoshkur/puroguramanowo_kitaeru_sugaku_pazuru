# P.191

from itertools import permutations


N = 7


if __name__ == '__main__':
    count = 0
    for tuple in permutations(range(1, N + 1)):
        array = list(tuple)
        for i in range(len(array)):
            j = array.index(i + 1)
            if i != j:
                array[i], array[j] = array[j], array[i]
                count += 1

    print(count)
