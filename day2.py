def is_invalid_id(num):
    """Check if a number is invalid (repeated pattern at least twice)"""
    s = str(num)
    length = len(s)
    
    # Try all possible pattern lengths (from 1 to length//2)
    # Pattern must repeat at least twice, so max pattern length is length//2
    for pattern_len in range(1, length // 2 + 1):
        # Check if the length is divisible by pattern_len
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            # Check if the entire string is this pattern repeated
            repeats = length // pattern_len
            if pattern * repeats == s:
                return True
    
    return False

def find_invalid_ids_in_range(start, end):
    """Find all invalid IDs in the given range"""
    invalid_ids = []
    count = 0
    for num in range(start, end + 1):
        if is_invalid_id(num):
            invalid_ids.append(num)
        count += 1
        # Progress indicator for large ranges
        if count % 100000 == 0:
            print(f"  ... checked {count} numbers so far in range {start}-{end}")
    return invalid_ids

def solve(input_string):
    """Solve the puzzle given the input string"""
    # Parse the ranges
    ranges = []
    for range_str in input_string.strip().split(','):
        start, end = map(int, range_str.split('-'))
        ranges.append((start, end))
    
    print(f"Processing {len(ranges)} ranges...\n")
    
    # Find all invalid IDs across all ranges
    all_invalid_ids = []
    for i, (start, end) in enumerate(ranges, 1):
        range_size = end - start + 1
        print(f"[{i}/{len(ranges)}] Range {start}-{end} (size: {range_size:,})")
        invalid_ids = find_invalid_ids_in_range(start, end)
        all_invalid_ids.extend(invalid_ids)
        if invalid_ids:
            print(f"  Found {len(invalid_ids)} invalid IDs: {invalid_ids[:5]}{'...' if len(invalid_ids) > 5 else ''}")
        else:
            print(f"  No invalid IDs found")
    
    # Sum them up
    total = sum(all_invalid_ids)
    print(f"\nTotal invalid IDs found: {len(all_invalid_ids)}")
    print(f"Total sum of invalid IDs: {total:,}")
    return total

# Test with the example
example_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

print("Testing with example:")
result = solve(example_input)
print(f"\nExpected: 1227775554")
print(f"Got: {result}")
print(f"Match: {result == 1227775554}")

print("\n" + "="*50)
print("Running with actual puzzle input:")
print("="*50)

actual_input = """61-71,12004923-12218173,907895-1086340,61083-74975,7676687127-7676868552,3328-4003,48-59,3826934-3859467,178-235,75491066-75643554,92-115,1487-1860,483139-586979,553489051-553589200,645895-722188,47720238-47818286,152157-192571,9797877401-9798014942,9326-11828,879837-904029,4347588-4499393,17-30,1-16,109218-145341,45794-60133,491-643,2155-2882,7576546102-7576769724,4104-5014,34-46,67594702-67751934,8541532888-8541668837,72-87,346340-480731,3358258808-3358456067,78265-98021,7969-9161,19293-27371,5143721-5316417,5641-7190,28793-36935,3232255123-3232366239,706-851,204915-242531,851-1135,790317-858666"""

actual_result = solve(actual_input)
print(f"\n*** ANSWER: {actual_result} ***")