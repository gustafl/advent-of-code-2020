f = open('input.txt', mode='rt', encoding='utf-8')
lines = f.readlines()
f.close()

my_pos = 0  # My position (0-30)
trees = 0  # Number of trees found

for line in lines:
    # Trim newline
    line = line.strip()
    # If we've reach outside the right border, adjust position
    if my_pos > len(line) - 1:
        my_pos = my_pos - len(line)
    # If it's a tree, count it
    if line[my_pos] == '#':
        trees += 1
    # Move to new position
    my_pos += 3

print("Answer: {}".format(trees))
