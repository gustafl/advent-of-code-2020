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


def get_seat(s):
    row = get_row(s)
    col = get_column(s)
    seat_id = row * 8 + col
    return seat_id


def main():
    highest_seat_id = 0
    seats = []
    with open('input.txt', mode='rt', encoding='utf-8') as f:
        for line in f:
            seat_id = get_seat(line)
            seats.append(seat_id)
            if seat_id > highest_seat_id:
                highest_seat_id = seat_id

    seats.sort()
    remaining = []

    for seat in seats:
        if seat - 1 in seats and seat + 1 in seats:
            remaining.append(seat)

    low = remaining[0]
    high = remaining[-1] + 1
    for x in range(low, high):
        if x not in seats:
            sys.stdout.write("Seat {} is missing!\n".format(x))


main()
