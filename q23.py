# P.101

MAX_GAMES = 24
START_COINS = 10


def game(coin: int, depth: int, memo: dict) -> int:
    key = f'{coin}_{depth}'
    if key in memo.keys():
        return memo[key]
    if coin == 0:
        return 0
    if depth == 0:
        return 1

    win = game(coin=coin + 1, depth=depth - 1, memo=memo)
    lose = game(coin=coin - 1, depth=depth - 1, memo=memo)
    memo[key] = win + lose
    return memo[key]


if __name__ == '__main__':
    memo = {}
    print(game(coin=10, depth=24, memo=memo))
