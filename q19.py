# P.87


from itertools import permutations


def get_primes(limit: int):
    primes = [2, 3,]
    for i in range(2, limit):
        for j in range(2, int(limit ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


if __name__ == '__main__':
    # primes = get_primes(limit=15)
    primes = [2, 3, 5, 7, 11, 13]
    saishou_suu = primes[-1] ** 2
    saishou_friend = []
    for prime in permutations(primes):
        friends = []
        for index in range(len(prime) - 1):
            friends.append(prime[index] * prime[index + 1])
        friends += map(lambda x: x ** 2, [prime[0], prime[-1]])
        if saishou_suu > max(friends):
            saishou_suu = max(friends)
            saishou_friend = friends
    print(saishou_suu)
    print(saishou_friend)
