# P.27

def cut_bar(sagyou_ninzuu: int, bou_no_nagasa: int, genzai_no_nagasa: int) -> int:
    if genzai_no_nagasa >= bou_no_nagasa:
        return 0
    elif genzai_no_nagasa < sagyou_ninzuu:
        return 1 + cut_bar(
            sagyou_ninzuu=sagyou_ninzuu,
            bou_no_nagasa=bou_no_nagasa,
            genzai_no_nagasa=genzai_no_nagasa * 2
        )
    else:
        return 1 + cut_bar(
            sagyou_ninzuu=sagyou_ninzuu,
            bou_no_nagasa=bou_no_nagasa,
            genzai_no_nagasa=genzai_no_nagasa + sagyou_ninzuu
        )


if __name__ == '__main__':
    print(cut_bar(sagyou_ninzuu=3, bou_no_nagasa=20, genzai_no_nagasa=1))
    print(cut_bar(sagyou_ninzuu=5, bou_no_nagasa=100, genzai_no_nagasa=1))
