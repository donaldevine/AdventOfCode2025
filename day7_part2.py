def count_quantum_timelines(input_text):
    """
    Count the number of unique timelines for a quantum tachyon particle.
    The particle takes BOTH paths at each splitter, creating multiple timelines.
    We need to count how many distinct final states exist.
    """
    lines = input_text.strip().split('\n')
    grid = [list(line) for line in lines]
    
    # Find the starting position 'S'
    start_col = None
    for col in range(len(grid[0])):
        if grid[0][col] == 'S':
            start_col = col
            break
    
    if start_col is None:
        print("Error: No starting position 'S' found")
        return 0
    
    # Track all active timeline positions
    # Use a set to track current positions, and count total timelines
    # Each position represents a distinct timeline state at that point
    current_positions = {(0, start_col)}
    
    # Process all positions row by row until all beams exit
    max_row = len(grid)
    
    for row in range(max_row):
        # Get all positions at current row
        positions_at_row = {(r, c) for r, c in current_positions if r == row}
        
        if not positions_at_row:
            continue
            
        # Remove processed positions from current set
        current_positions -= positions_at_row
        
        # Process each position
        for pos_row, col in positions_at_row:
            # Check bounds
            if col < 0 or col >= len(grid[0]):
                continue
                
            current_cell = grid[pos_row][col]
            
            # If we hit a splitter
            if current_cell == '^':
                # Particle goes both left and right, then continues downward
                current_positions.add((pos_row + 1, col - 1))
                current_positions.add((pos_row + 1, col + 1))
            else:
                # Empty space or 'S' - continue moving down
                current_positions.add((pos_row + 1, col))
    
    # Count final timeline endpoints (positions that exited the grid)
    # We need to track all the paths, not just final positions
    # Let me reconsider the approach...
    
    return len(current_positions)


def count_quantum_timelines_v2(input_text):
    """
    Count timelines by tracking all unique paths through the manifold.
    Each complete path from S to an exit represents one timeline.
    """
    import sys
    sys.setrecursionlimit(50000)
    
    lines = input_text.strip().split('\n')
    grid = [list(line) for line in lines]
    
    # Find the starting position 'S'
    start_col = None
    for col in range(len(grid[0])):
        if grid[0][col] == 'S':
            start_col = col
            break
    
    if start_col is None:
        print("Error: No starting position 'S' found")
        return 0
    
    # Use memoization to avoid recalculating paths
    memo = {}
    
    def count_paths(row, col):
        """Count all paths from this position to exit."""
        # Check if we've exited the grid
        if row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 1  # This is one complete path
        
        # Check memo
        if (row, col) in memo:
            return memo[(row, col)]
        
        current_cell = grid[row][col]
        
        if current_cell == '^':
            # At a splitter, particle goes both ways
            result = count_paths(row + 1, col - 1) + count_paths(row + 1, col + 1)
        else:
            # Continue downward
            result = count_paths(row + 1, col)
        
        memo[(row, col)] = result
        return result
    
    total_timelines = count_paths(0, start_col)
    return total_timelines


# Read input
with open('day7_input.txt', 'r') as f:
    puzzle_input = f.read()

# Solve
result = count_quantum_timelines_v2(puzzle_input)
print(f"Total timelines: {result}")
