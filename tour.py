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
    Displays the chess board with move numbers
    Parameters:
        board: NxN matrix with move numbers
    """
    board_size = len(board)
    total_squares = board_size * board_size - 1
    # Calculate number of digits needed for the largest number
    width = len(str(total_squares))
    
    for row in board:
        # Format each number with consistent width
        print(" ".join(f"{num:0{width}d}" if num != -1 else "-"*width for num in row))
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
        counter: current move number
    Returns:
        boolean: True if solution found, False otherwise
    """
    board_size = len(board)
    total_squares = board_size * board_size
    
    # Base case: all squares visited
    if counter == total_squares:
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

def find_solutions_no_backtrack(board, row, col, counter):
    """
    Non-backtracking version of Warnsdorff's algorithm
    Parameters:
        board: current board state
        row, col: current position
        counter: current move number
    Returns:
        boolean: True if solution found, False otherwise
    """
    board_size = len(board)
    total_squares = board_size * board_size
    
    # Base case: all squares visited
    if counter == total_squares:
        print("Solution found:")
        print_board(board)
        return True

    possible_moves = []
    moves = [
        (-2, +1), (+2, +1), (-2, -1), (+2, -1),
        (-1, +2), (-1, -2), (+1, +2), (+1, -2)
    ]
    
    # Get all valid moves and their degrees
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if is_valid(board, new_row, new_col):
            degree = count_onward_moves(board, new_row, new_col)
            possible_moves.append((new_row, new_col, degree))
    
    # If no moves available, fail immediately
    if not possible_moves:
        return False
    
    # Take the move with minimum degree (most constrained)
    possible_moves.sort(key=lambda x: x[2])
    best_move = possible_moves[0]
    new_row, new_col, _ = best_move
    
    # Make the move (no backtracking)
    board[new_row][new_col] = counter
    return find_solutions_no_backtrack(board, new_row, new_col, counter + 1)

def get_valid_board_size():
    """
    Gets a valid board size from user input
    Returns:
        int: validated board size
    """
    while True:
        try:
            size = int(input("Enter board size (minimum 5): "))
            if size < 5:
                print("Board size must be at least 5x5")
                continue
            return size
        except ValueError:
            print("Please enter a valid number")

def get_valid_start_position(board_size):
    """
    Gets valid starting coordinates from user input
    Parameters:
        board_size: size of the chess board
    Returns:
        tuple: (row, col) starting position
    """
    while True:
        try:
            row = int(input(f"Enter starting row (0-{board_size-1}): "))
            col = int(input(f"Enter starting column (0-{board_size-1}): "))
            if 0 <= row < board_size and 0 <= col < board_size:
                return row, col
            print(f"Position must be within 0 and {board_size-1}")
        except ValueError:
            print("Please enter valid numbers")

def main():
    # Get board size from user
    board_size = get_valid_board_size()
    
    # Get starting position
    start_row, start_col = get_valid_start_position(board_size)
    
    # Try non-backtracking version first
    print("\nAttempting non-backtracking solution...")
    board = [[-1 for x in range(board_size)] for x in range(board_size)]
    board[start_row][start_col] = 0
    if not find_solutions_no_backtrack(board, start_row, start_col, 1):
        print("No solution found with non-backtracking method.")
        
        # If non-backtracking fails, try the original version
        print("\nAttempting solution with backtracking...")
        board = [[-1 for x in range(board_size)] for x in range(board_size)]
        board[start_row][start_col] = 0
        if not find_solutions(board, start_row, start_col, 1):
            print("No solution found with backtracking method either.")

if __name__ == "__main__":
    main()
