# P.231

def cut_cake(w: int, h: int, diff: int, memo: dict) -> dict:
    if w < h:
        w, h = h, w

    key = tuple([w, h, diff])
    if key in memo:
        return memo[key]

    if w == 1 and h == 1:
        memo[key] = 0 if diff == 1 else float('inf')
        return memo[key]

    if w * h / 2 < diff:
        return float('inf')

    tate = [h + cut_cake(w=w - i, h=h, diff=i * h - diff, memo=memo) for i in range(1, w // 2 + 1)]
    yoko = [w + cut_cake(w=w, h=h - i, diff=w * i - diff, memo=memo) for i in range(1, h // 2 + 1)]
    memo[key] = min(tate + yoko)
    return memo[key]


if __name__ == '__main__':
    memo = {}
    print(cut_cake(w=16, h=12, diff=0, memo=memo))
