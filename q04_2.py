# P.27

def join_bar(sagyou_ninzuu: int, bou_no_nagasa: int) -> None:
    count = 0
    genzai_no_nagasa = 1
    while bou_no_nagasa > genzai_no_nagasa:
        genzai_no_nagasa += genzai_no_nagasa if genzai_no_nagasa < sagyou_ninzuu else sagyou_ninzuu
        count += 1
    print(count)


if __name__ == '__main__':
    join_bar(sagyou_ninzuu=3, bou_no_nagasa=20)
    join_bar(sagyou_ninzuu=5, bou_no_nagasa=100)
