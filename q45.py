# P.187

from itertools import product


def get_primes(limit: int):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    for i in range(2, limit):
        for j in range(2, int(limit ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


if __name__ == '__main__':
    primes = [i for i in get_primes(limit=1000) if i > 100]
    prime_h = {0: []}
    for prime in primes:
        sentou = prime // 100
        prime_h[sentou] = [i for i in primes if i // 100 == sentou]
    count = 0
    for r1 in primes:
        for c1, c2, c3 in product(prime_h[r1 // 100], prime_h[r1 % 100 // 10], prime_h[r1 % 10]):
            r2 = (c1 % 100 // 10) * 100 + (c2 % 100 // 10) * 10 + (c3 % 100 // 10)
            r3 = (c1 % 10) * 100 + (c2 % 10) * 10 + (c3 % 10)
            if r2 in primes and r3 in primes:
                if len(set([r1, r2, r3, c1, c2, c3])) == 6:
                    count += 1
    print(count)
