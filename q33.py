# P.139

import polars as pl


def search(list_: list, len_: int):
    global count

    if len(list_) == 1:
        count += len_ - 1
    else:
        for k in set(l[0: len_] for l in list_):
            kouho = [v for v in list_ if v.startswith(k[0: len_])]
            search(list_=kouho, len_=len_ + 1)


if __name__ == '__main__':
    count = 0
    df = pl.read_csv(source='sample/q33.csv')
    ku = df['上の句かな'].to_list()
    search(list_=ku, len_=1)
    ku = df['下の句かな'].to_list()
    search(list_=ku, len_=1)
    print(count)
