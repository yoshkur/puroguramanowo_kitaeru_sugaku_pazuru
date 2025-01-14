# P.37
from datetime import datetime


if __name__ == '__main__':
    from_bin = bin(19641010)
    from_bin_pick = from_bin[2 + 4: 2 + 4 + 8]
    from_left = int(from_bin_pick, 2)
    to_bin = bin(20200724)
    to_bin_pick = to_bin[2 + 4: 2 + 4 + 8]
    to_left = int(to_bin_pick, 2)
    for i in range(from_left, to_left + 1):
        l = bin(i)[2:]
        if len(l) == 7:
            l = f'0{l}'
        r = l[::-1]
        for m in range(2):
            value = f'1001{l}{m}{r}1001'
            try:
                date_ = int(value, 2)
                print(datetime.strptime(str(date_), r'%Y%m%d'))
            except:
                pass
