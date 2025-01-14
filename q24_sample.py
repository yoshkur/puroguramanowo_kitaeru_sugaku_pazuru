# This code is a Ruby to Python translation of a board game logic.
# Set of possible moves for two pieces
board = [[1, 2], [2, 3], [7, 8], [8, 9],
         [1, 4], [3, 6], [4, 7], [6, 9]]

# Add individual moves
for i in range(1, 10):
    board.append([i])

memo = {(): 1}

def strike(current_board):
    # Use the value if already explored
    if tuple(map(tuple, current_board)) in memo:
        return memo[tuple(map(tuple, current_board))]
    
    count = 0
    for b in current_board:
        # Exclude moves that contain numbers already taken
        next_board = [i for i in current_board if len(set(b) & set(i)) == 0]
        count += strike(next_board)
    
    memo[tuple(map(tuple, current_board))] = count
    return count

print(strike(board))
