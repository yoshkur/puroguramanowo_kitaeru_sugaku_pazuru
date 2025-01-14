# P.283

PAIR = 6

START = list(range(1, PAIR * 2)) + [0]
GOAL = [0] + list(range(2, PAIR * 2)) + [1]


def exists_element(list_a: list, list_b: list):
    for element in list_a:
        if element in list_b:
            return True
    return False


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
    fw = [START]
    fw_log = [START]
    bw = [GOAL]
    bw_log = [GOAL]
    count = 0

    while True:
        next_fw = throwable(balls=fw)
        fw = [ball for ball in next_fw if ball not in fw_log]
        fw_log.extend(next_fw)
        count += 1
        if exists_element(list_a=fw, list_b=bw):
            break

        next_bw = throwable(balls=bw)
        bw = [ball for ball in next_bw if ball not in bw_log]
        bw_log.extend(next_bw)
        count += 1
        if exists_element(list_a=fw, list_b=bw):
            break

    print(count)
