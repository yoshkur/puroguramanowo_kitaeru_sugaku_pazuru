# P.37
from datetime import date
from dateutil.relativedelta import relativedelta


if __name__ == '__main__':
    start_ = date(1964, 10, 10)
    end_ = date(2020, 7, 24)
    end_int = int(end_.strftime(r'%Y%m%d'))

    current_date = start_
    date_ = int(current_date.strftime(r'%Y%m%d'))
    while date_ <= end_int:
        bin_date = bin(date_)
        reversed_bin_date = bin_date[2:][::-1]
        reversed_dec_date = int(reversed_bin_date, 2)
        if date_ == reversed_dec_date:
            print(date_)
        current_date += relativedelta(days=1)
        date_ = int(current_date.strftime(r'%Y%m%d'))
