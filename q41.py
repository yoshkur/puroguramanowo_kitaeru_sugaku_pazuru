# P.171

if __name__ == '__main__':
    ip = []
    # for i in range(1 << 16):
    for i in range(2 ** 16):
        j = int(f'{i:016b}'[::-1], 2)

        s = f'{i >> 8}.{i & 0xff}.{j >> 8}.{j & 0xff}'

        if len(set(s)) == 11:
            ip.append(s)

    print(len(ip))
    print(ip)
