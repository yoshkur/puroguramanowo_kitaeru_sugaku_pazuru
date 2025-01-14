# P.57

from itertools import count


if __name__ == '__main__':
    for index in count():
        suji_str = f'{index ** 0.5:.10f}'
        moji_list = list(set(list(suji_str.replace('.', '')[:10])))
        if len(moji_list) == 10:
            break
        index += 1
    print(index)

    for index in count():
        suji_str = f'{index ** 0.5:.10f}'
        seisubu, shosubu = suji_str.split('.')
        moji_list = list(set(list(shosubu[:10])))
        if len(moji_list) == 10:
            break
        index += 1
    print(index)
