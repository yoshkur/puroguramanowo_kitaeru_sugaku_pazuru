# P.95

if __name__ == '__main__':
    count = 0
    line = 1
    row = [1]

    while count < 2014:
        next_row = [1]
        for index in range(len(row) - 1):
            cell = row[index] ^ row[index + 1]
            next_row.append(cell)
            if cell == 0:
                count += 1
        next_row.append(1)
        line += 1
        row = next_row

    print(line)
