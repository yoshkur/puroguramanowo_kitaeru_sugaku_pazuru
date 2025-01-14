# P.95

if __name__ == '__main__':
    count = 0
    line = 1
    row = 1

    while count < 2014:
        row ^= row << 1
        count += bin(row)[2:].count('0')
        line += 1

    print(line)
