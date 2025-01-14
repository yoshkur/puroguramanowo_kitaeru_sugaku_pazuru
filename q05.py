# P.31
from itertools import combinations_with_replacement


RYOUGAE_KINGAKU = 1000
MAX_COINS = 15
COINS = [10, 50, 100, 500]

if __name__ == '__main__':
    count = 0
    for maisu in range(2, MAX_COINS + 1):
        for coins in combinations_with_replacement(COINS, maisu):
            if sum(coins) == RYOUGAE_KINGAKU:
                count += 1
    print(count)
