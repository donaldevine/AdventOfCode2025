def solve_tachyon_manifold(input_text):
    """
    Simulate tachyon beams splitting through a manifold.
    - Beams start at 'S' and move downward
    - '.' is empty space (beam passes through)
    - '^' is a splitter (beam stops, two new beams emit from immediate left and right, continuing downward)
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
    
    # Track splits
    # All beams always move downward
    split_count = 0
    active_beams = [(0, start_col)]  # (row, col)
    processed = set()
    
    while active_beams:
        row, col = active_beams.pop(0)
        
        # Skip if we've already processed this position
        if (row, col) in processed:
            continue
        processed.add((row, col))
        
        # Check bounds
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            continue
        
        current_cell = grid[row][col]
        
        # If we hit a splitter
        if current_cell == '^':
            split_count += 1
            # Create two new beams at immediate left and right positions
            # Both continue moving downward from next row
            active_beams.append((row + 1, col - 1))
            active_beams.append((row + 1, col + 1))
        else:
            # Empty space or 'S' - continue moving down
            active_beams.append((row + 1, col))
    
    return split_count


# Read input
with open('day7_input.txt', 'r') as f:
    puzzle_input = f.read()

# Solve
result = solve_tachyon_manifold(puzzle_input)
print(f"Total beam splits: {result}")
