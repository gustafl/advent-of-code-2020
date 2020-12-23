import sys

non_blank_count = 0  # Number of non-blank lines in file

with open('input.txt', mode='rt', encoding='utf-8') as f:
    lines = f.readlines()
    f.seek(0)
    for line in f:
        if line.strip():
            non_blank_count += 1

my_pos = 0  # Next horizontal position (0-30)
result = 1  # Final result
slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]
sr = []  # Slope results

for slope in slopes:
    my_pos = 0  # Always start on position 0
    trees = 0  # Number of trees found in current slope
    step = slope[1]  # Number of steps to move vertically between loop increments
    for i in range(0, non_blank_count, step):
        # Get current line
        line = lines[i].strip()
        # If we've reached outside the right border, adjust the position
        if my_pos > len(line) - 1:
            my_pos = my_pos % len(line)
        # If it's a tree, count it
        if line[my_pos] == '#':
            trees += 1
        # Move to new position
        my_pos += slope[0]
    sr.append(trees)
    sys.stdout.write('{} trees encountered on the {}:{} slope.\n'.format(trees, slope[0], slope[1]))
    result *= trees  # Result is 1 before first multiplication

print("{} * {} * {} * {} * {} = {}".format(sr[0], sr[1], sr[2], sr[3], sr[4], result))
