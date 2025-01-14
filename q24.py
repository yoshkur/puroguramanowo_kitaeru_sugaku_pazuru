# P.103

def strike(board: list, memo: dict) -> int:
    key = tuple(map(tuple, board))

    if key in memo.keys():
        return memo[key]

    count = 0
    for b in board:
        next_board = [i for i in board if len(set(b) & set(i)) == 0]
        count += strike(board=next_board, memo=memo)

    memo[key] = count
    return count


if __name__ == '__main__':
    board = [[1, 2], [2, 3], [7, 8], [8, 9], [1, 4], [3, 6], [4, 7], [6, 9]]
    for i in range(9):
        board.append([i + 1])

    memo = {(): 1}
    print(strike(board=board, memo=memo))
