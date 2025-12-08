def solve_worksheet_rtl(input_text):
    # Don't strip the input - preserve leading spaces!
    lines = input_text.split('\n')
    # Remove empty lines at the end if any
    while lines and not lines[-1].strip():
        lines.pop()
    
    # Find the maximum line length to handle all columns
    max_len = max(len(line) for line in lines)
    
    # Pad all lines to the same length
    padded_lines = [line.ljust(max_len) for line in lines]
    
    # Transpose to get columns
    columns = []
    for col_idx in range(max_len):
        column = ''.join(padded_lines[row_idx][col_idx] for row_idx in range(len(padded_lines)))
        columns.append(column)
    
    # Group columns into problems (separated by all-space columns)
    problems = []
    current_problem = []
    
    for idx, col in enumerate(columns):
        if col.strip() == '':  # All spaces - separator
            if current_problem:
                problems.append(current_problem)
                current_problem = []
        else:
            current_problem.append(col)
    
    # Don't forget the last problem
    if current_problem:
        problems.append(current_problem)
    
    # Solve each problem - read each column as a separate number (RTL processing)
    results = []
    for idx, problem in enumerate(problems):
        # Get the operation from the last row of the first column
        operation = problem[0][-1]
        
        # Each column represents one number, read top-to-bottom (excluding operation row)
        # But process columns right-to-left
        numbers = []
        for col_idx in range(len(problem) - 1, -1, -1):  # Right to left
            col = problem[col_idx]
            # Read digits top-to-bottom, excluding last row (operation)
            digits = [ch for ch in col[:-1] if ch.isdigit()]
            if digits:
                num = int(''.join(digits))
                numbers.append(num)
        
        # Calculate result
        if operation == '+':
            result = sum(numbers)
        elif operation == '*':
            result = 1
            for num in numbers:
                result *= num
        else:
            result = 0
        
        results.append(result)
    
    grand_total = sum(results)
    print(f"\nGrand Total: {grand_total}")
    return grand_total


with open('day6_input.txt', 'r') as f:
    puzzle_input = f.read()

print("Puzzle Solution (Part 2 - Right-to-Left):")
solve_worksheet_rtl(puzzle_input)
