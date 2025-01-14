# P.19
import itertools
import re


ENZANSHI = ['*', '']

if __name__ == '__main__':
    for index, enzanshi_1, enzanshi_2, enzanshi_3 in itertools.product(range(1000, 10000), ENZANSHI, ENZANSHI, ENZANSHI):
        index_str = str(index)
        keisanshiki = index_str[3] + enzanshi_1 + index_str[2] + enzanshi_2 + index_str[1] + enzanshi_3 + index_str[0]
        keisanshiki = re.sub(r'0(\d)', r'\1', keisanshiki)
        if len(keisanshiki) < 5:
            continue
        if index == eval(keisanshiki):
            print(f'{keisanshiki} = {index}')
