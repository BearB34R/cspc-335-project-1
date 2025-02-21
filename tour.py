def is_valid(board, new_row, new_col):
    """
    Check if the new position is within bounds and has not been visited.
    """
    board_size = len(board)
    if new_row < 0 or new_row >= board_size:
        return False
    if new_col < 0 or new_col >= board_size:
        return False
    if board[new_row][new_col] != -1:
        return False
    return True

def print_board(board):
    """
    Print the board in a formatted way.
    """
    for row in board:
        print(" ".join(f"{num:02d}" for num in row))
    print()

def count_onward_moves(board, row, col):
    """Count possible moves from a given position"""
    count = 0
    moves = [
        (-2, +1), (+2, +1), (-2, -1), (+2, -1),
        (-1, +2), (-1, -2), (+1, +2), (+1, -2)
    ]
    
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if is_valid(board, new_row, new_col):
            count += 1
    return count

def find_solutions(board, row, col, counter):
    if counter == 64:
        print("Solution found:")
        print_board(board)
        return True

    # Get all possible moves and their degrees (number of onward moves)
    possible_moves = []
    moves = [
        (-2, +1), (+2, +1), (-2, -1), (+2, -1),
        (-1, +2), (-1, -2), (+1, +2), (+1, -2)
    ]
    
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if is_valid(board, new_row, new_col):
            # Count available moves from the next position
            degree = count_onward_moves(board, new_row, new_col)
            possible_moves.append((new_row, new_col, degree))
    
    # Sort moves by degree (ascending) - Warnsdorff's rule
    possible_moves.sort(key=lambda x: x[2])
    
    # Try moves in order of increasing degree
    for new_row, new_col, _ in possible_moves:
        board[new_row][new_col] = counter
        if find_solutions(board, new_row, new_col, counter + 1):
            return True
        board[new_row][new_col] = -1

    return False

def main():
    board_size = 8
    # Initialize an 8x8 board with -1 (indicating unvisited squares)
    board = [[-1 for _ in range(board_size)] for _ in range(board_size)]
    
    # Starting position (top left corner)
    board[0][0] = 0

    if not find_solutions(board, 0, 0, 1):
        print("No solution found.")

if __name__ == "__main__":
    main()
