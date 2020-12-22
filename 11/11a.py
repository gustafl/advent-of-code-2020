import sys


def get_input(file):
    with open(file, 'rt', encoding='utf8') as f:

        # Get lines
        lines = []
        for line in f.readlines():
            line = line.strip()
            lines.append(line)

        # Define matrix
        height = len(lines)
        width = len(lines[0])
        matrix = [['' for x in range(width)] for y in range(height)]

        # Populate matrix
        for y in range(height):
            line = lines[y]
            for x in range(width):
                char = line[x]
                matrix[y][x] = char

        return matrix


def get_adjecent_occupied(matrix, y, x):
    height = len(matrix)
    width = len(matrix[0])
    count = 0
    for row in range(y - 1, y + 2):
        if row < 0 or row > height - 1:
            continue
        for cell in range(x - 1, x + 2):
            if cell < 0 or cell > width - 1:
                continue
            if row == y and cell == x:  # Skip the middle cell
                continue
            if matrix[row][cell] == '#':
                count += 1

    return count


def refresh_matrix(matrix):
    changed_matrix = matrix.copy()
    height = len(matrix)
    width = len(matrix[0])
    count = 0
    for y in range(height):
        for x in range(width):
            char = matrix[y][x]
            adj_occ = get_adjecent_occupied(matrix, y, x)  # Get the number of neighbours
            if char == 'L' and adj_occ == 0:  # If seat is empty and there are no occupied adjacent seats
                changed_matrix[y][x] = '#'
                count += 1
            elif char == '#' and adj_occ >= 4:  # If seat is occupied and four or more adjacent seats are occupied
                changed_matrix[y][x] = 'L'
                count += 1

    matrix = changed_matrix
    print_matrix(matrix)
    return count


def print_matrix(matrix):
    height = len(matrix)
    width = len(matrix[0])
    for i in range(height):
        for j in range(width):
            sys.stdout.write("{}  ".format(matrix[i][j]))
        sys.stdout.write("\n")
    sys.stdout.write("\n")


def main():
    matrix = get_input('sample.txt')
    print_matrix(matrix)
    changes = 0
    while new_changes := refresh_matrix(matrix):
        if new_changes == changes:
            break
        else:
            changes = new_changes

    sys.stdout.write("Answer: {}\n".format(changes))


main()


