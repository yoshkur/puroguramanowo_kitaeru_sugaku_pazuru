# P.71

DANSU = 10
MAX_STEPS = 4


if __name__ == '__main__':
    idou_ichi_shuukei = [0] * (DANSU + 1)
    count = 0
    idou_ichi_shuukei[DANSU] = 1
    for idou_kaisuu in range(DANSU):
        for idou_moto in range(DANSU + 1):
            for idou_ryou in range(1, MAX_STEPS + 1):
                if idou_ryou > idou_moto:
                    break
                idou_ichi_shuukei[idou_moto - idou_ryou] += idou_ichi_shuukei[idou_moto]
            idou_ichi_shuukei[idou_moto] = 0
        if idou_kaisuu % 2:
            count += idou_ichi_shuukei[0]

    print(count)
