# Knight's Tour using Warnsdorff's Rule

Warnsdorff's rule is a heuristic method for finding a knight's tour on a chessboard. The rule states that the knight should always move to the square from which the knight will have the fewest onward moves.

## Algorithm Pseudocode

```
function KnightTour(board, start_position):
    1. Initialize board with all squares marked as unvisited
    2. Place knight at start_position and mark as visited (move #0)
    3. For moves from 1 to 63:
        a. Get all valid unvisited neighboring positions
        b. For each valid position:
            - Count number of onward moves (degree)
            - Store position and its degree
        c. Sort positions by degree (ascending)
        d. Move knight to position with minimum degree
        e. Mark new position with current move number
    4. If all squares are visited (move #63 completed)
        Return success
    5. If no moves possible
        Return failure

function CountOnwardMoves(board, position):
    1. Initialize count = 0
    2. For each possible knight move from position:
        If move leads to valid unvisited square:
            Increment count
    3. Return count

function IsValid(board, position):
    Return true if:
        - Position is within board boundaries
        - Position has not been visited
    Otherwise return false
```

## Implementation Details

The algorithm uses the following key components:
- A board representation (typically an N×N matrix)
- Move validation to ensure knight stays within bounds
- Degree calculation for each possible move
- Backtracking when no valid moves are available

The knight has up to 8 possible moves from any position. The success of Warnsdorff's rule comes from always choosing the move that has the fewest onward moves available, which helps avoid dead ends in the tour.

## Data Structure and Complexity Analysis

### Data Structures Used
- **2D Array (Matrix)**: The main board is represented as an N×N matrix where N=8 for a standard chessboard
- **List**: Used to store possible moves and their degrees during move selection

### Time Complexity
- **Overall Algorithm**: O(N²) in practice with Warnsdorff's heuristic
  - Without the heuristic, it would be O(8^(N²)) using naive backtracking
- **Move Validation**: O(1)
- **Count Onward Moves**: O(8) = O(1) as it checks 8 possible moves
- **Move Selection**: O(8 log 8) = O(1) for sorting possible moves

### Space Complexity
- **Board Storage**: O(N²) for the N×N matrix
- **Recursive Call Stack**: O(N²) in worst case
- **Temporary Move Storage**: O(1) as it stores max 8 possible moves

### Performance Note
While the theoretical worst-case complexity could be higher, Warnsdorff's rule drastically improves practical performance by intelligently selecting moves that are more likely to lead to a solution.