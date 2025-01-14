# P.283
# 数分経っても終わらない。


PAIR = 6

START = list(range(1, PAIR * 2)) + [0]
GOAL = [0] + list(range(2, PAIR * 2)) + [1]


def throwable(balls: list):
    result = []
    for ball in balls:
        c = ball.index(0)
        p = (c + PAIR) % (PAIR * 2)
        for d in [-1, 0, 1]:
            if (p + d) // PAIR == p // PAIR:
                ball[c], ball[p + d] = ball[p + d], ball[c]
                result.append(ball.copy())
                ball[c], ball[p + d] = ball[p + d], ball[c]
    return result


if __name__ == '__main__':
    balls = [START]
    log = [START]
    count = 0
    while GOAL not in balls:
        next_balls = throwable(balls=balls)
        balls = [ball for ball in next_balls if ball not in log]
        log.extend(next_balls)
        count += 1

    print(count)
