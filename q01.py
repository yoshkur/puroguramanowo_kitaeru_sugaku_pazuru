# P.15
def is_kaibun_su(original_value: str) -> bool:
    reversed_value = original_value[::-1]
    return original_value == reversed_value


if __name__ == '__main__':
    check_value = 11
    while True:
        if not is_kaibun_su(original_value=str(check_value)):
            check_value += 2
            continue
        if not is_kaibun_su(original_value=oct(check_value)[2:]):
            check_value += 2
            continue
        if not is_kaibun_su(original_value=bin(check_value)[2:]):
            check_value += 2
            continue
        print(check_value)
        break
