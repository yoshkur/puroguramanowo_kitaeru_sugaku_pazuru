# P.147

if __name__ == '__main__':
    n = [i + 1 for i in range(50) if i % 2 or i % 5]
    answer = []
    k = 1
    while len(n):
        x = int(bin(k)[2:]) * 7
        x_str = str(x)
        if x_str.find('0') > 0:
            for i in n:
                if x % i == 0:
                    if x_str == x_str[::-1]:
                        answer.append(i)
                    n.remove(i)
        k += 1
    print(sorted(answer))
