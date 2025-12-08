def solve_worksheet(input_text):
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
    
    # Solve each problem
    results = []
    for idx, problem in enumerate(problems):
        # Combine columns of the problem into rows
        problem_rows = []
        for row_idx in range(len(padded_lines)):
            row = ''.join(problem[col_idx][row_idx] for col_idx in range(len(problem)))
            problem_rows.append(row.strip())
        
        # Remove empty rows
        problem_rows = [r for r in problem_rows if r]
        
        # Last row is the operation - take first non-space character
        operation = problem_rows[-1].replace(' ', '')[0] if problem_rows[-1].replace(' ', '') else '+'
        # Parse numbers - the entire row (after stripping) should be the number
        numbers = []
        for r in problem_rows[:-1]:
            # The whole stripped row should be a single number
            if r:
                # Remove all spaces to get the full number
                num_str = r.replace(' ', '')
                if num_str:
                    numbers.append(int(num_str))
        
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

print("\n\nPuzzle Solution:")
solve_worksheet(puzzle_input)
