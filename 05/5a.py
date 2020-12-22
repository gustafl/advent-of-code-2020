import sys


def get_row(line):
    low = 0
    high = 127
    for i in range(0, 7):
        char = line[i]
        diff = int((high + 1 - low) / 2)
        if char == 'B':
            low += diff
        elif char == 'F':
            high -= diff

        if low == high:
            return low


def get_column(line):
    low = 0
    high = 7
    for i in range(7, 10):
        char = line[i]
        diff = int((high + 1 - low) / 2)
        if char == 'R':
            low += diff
        elif char == 'L':
            high -= diff

        if low == high:
            return low


def get_seat_id(s):
    row = get_row(s)
    col = get_column(s)
    seat_id = row * 8 + col
    return seat_id


def main():
    highest_seat_id = 0
    with open('input.txt', mode='rt', encoding='utf-8') as f:
        for line in f:
            seat_id = get_seat_id(line)
            if seat_id > highest_seat_id:
                highest_seat_id = seat_id

    sys.stdout.write("\nThe highest seat ID is {}.\n".format(highest_seat_id))


main()
