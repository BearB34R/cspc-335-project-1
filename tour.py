def is_valid(board, new_row, new_col):
    """
    Validates if a move is legal on the chess board
    Parameters:
        board: 8x8 matrix representing the chess board
        new_row, new_col: coordinates of the proposed move
    Returns:
        boolean: True if move is valid, False otherwise
    """
    board_size = len(board)
    # Check board boundaries
    if new_row < 0 or new_row >= board_size:
        return False
    if new_col < 0 or new_col >= board_size:
        return False
    # Check if square is already visited (-1 means unvisited)
    if board[new_row][new_col] != -1:
        return False
    return True

def print_board(board):
    """
    Displays the chess board with move numbers (00-63)
    Parameters:
        board: 8x8 matrix with move numbers
    """
    for row in board:
        # Format each number with 2 digits (00-63)
        print(" ".join(f"{num:02d}" for num in row))
    print()

def count_onward_moves(board, row, col):
    """
    Implements Warnsdorff's rule by counting available next moves
    Parameters:
        board: current board state
        row, col: current knight's position
    Returns:
        int: number of possible future moves
    """
    count = 0
    # All possible L-shaped moves a knight can make
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
    """
    Recursive function implementing Warnsdorff's algorithm
    Parameters:
        board: current board state
        row, col: current position
        counter: current move number (1-63)
    Returns:
        boolean: True if solution found, False otherwise
    """
    # Base case: all squares visited
    if counter == 64:
        print("Solution found:")
        print_board(board)
        return True

    # STEP 1: Get all possible moves and their degrees
    possible_moves = []
    moves = [
        (-2, +1), (+2, +1), (-2, -1), (+2, -1),
        (-1, +2), (-1, -2), (+1, +2), (+1, -2)
    ]
    
    # STEP 2: Calculate degree (number of onward moves) for each possible move
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if is_valid(board, new_row, new_col):
            degree = count_onward_moves(board, new_row, new_col)
            possible_moves.append((new_row, new_col, degree))
    
    # STEP 3: Apply Warnsdorff's rule - sort by least number of onward moves
    possible_moves.sort(key=lambda x: x[2])
    
    # STEP 4: Try each move, starting with the most constrained ones
    for new_row, new_col, x in possible_moves:
        board[new_row][new_col] = counter  # Make move
        if find_solutions(board, new_row, new_col, counter + 1):
            return True
        board[new_row][new_col] = -1  # Backtrack

    return False

def main():
    board_size = 8
    # Create 8x8 board initialized with -1 (unvisited)
    board = [[-1 for x in range(board_size)] for x in range(board_size)]
    
    # Set starting position and mark it as visited (move #0)
    start_row, start_col = 2, 7
    board[start_row][start_col] = 0

    # Start the tour from position (2,7)
    if not find_solutions(board, start_row, start_col, 1):
        print("No solution found.")

if __name__ == "__main__":
    main()
