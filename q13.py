# P.61

from itertools import permutations


ENZANSHI = list('+-*/=')

if __name__ == '__main__':
    expression = 'READ+WRITE+TALK==SKILL'
    nums = expression
    for enzanshi_ in ENZANSHI:
        nums = nums.replace(enzanshi_, '')
    chars = list(set(list(nums)))

    count = 0
    for seq in permutations(range(10), len(chars)):
        seq_num_str = ''.join(map(str, seq))
        shiki = expression.translate(str.maketrans(''.join(chars), seq_num_str))

        if shiki[0] == '0':
            continue
        exist_zero_begin = False
        for enzanshi_ in ENZANSHI:
            if f'{enzanshi_}0' in shiki:
                exist_zero_begin = True
                break
        if exist_zero_begin:
            continue

        if eval(shiki):
            print(shiki)
            count += 1

    print(count)
