# P.53

# 求められている5つの答えに、例で記載されている6個分を加えた答えを返す。
ANS_COUNT = 5 + 6


def fibonacci():
    value_a = value_b = 1
    while True:
        next_value = value_a + value_b
        yield next_value

        value_a, value_b = value_b, next_value


def is_divid(number: int) -> bool:
    number_str = str(number)
    keta_suji_list = map(int, list(number_str))

    if not number % sum(keta_suji_list):
        return True
    else:
        return False


if __name__ == '__main__':
    anser_list = []
    for number in fibonacci():
        if is_divid(number=number):
            anser_list.append(number)

        if not len(anser_list) < ANS_COUNT:
            break

    print(anser_list)
