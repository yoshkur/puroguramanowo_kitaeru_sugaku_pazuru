# P.79

NINZUU = 30


if __name__ == '__main__':
    boy, girl = 1, 0
    for i in range(NINZUU):
        boy, girl = boy + girl, boy
    print(boy + girl)
