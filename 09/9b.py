import itertools
import sys


def get_input(file):
    lines = []
    with open(file, mode='rt', encoding='utf-8') as f:
        for line in f:
            number = int(line)
            lines.append(number)

    return lines


def find_bad_number(lines):
    offset = 25
    preamble_start = 0
    preamble = lines[preamble_start:preamble_start + offset]
    for i in range(offset, len(lines) - offset):
        number = lines[i]
        valid = False
        for a, b in itertools.combinations(preamble, 2):
            if a + b == number:
                valid = True
                break
        if not valid:
            return number
        preamble_start += 1
        preamble = lines[preamble_start:preamble_start + offset]


def try_group(numbers, index, bad_number):
    group = []
    for i in range(index, len(numbers)):
        number = numbers[i]
        group.append(number)
        group_sum = sum(group)
        if group_sum < bad_number:
            continue
        elif group_sum > bad_number:
            return
        elif group_sum == bad_number:
            return group


def main():
    lines = get_input('input.txt')
    bad_number = find_bad_number(lines)
    answer = 0

    for i in range(0, len(lines)):
        group = try_group(lines, i, bad_number)
        if not group:
            continue
        else:
            group.sort()
            first = group[0]
            last = group[-1]
            answer = first + last
            break

    sys.stdout.write("Answer: {}\n".format(answer))
    sys.exit(0)


main()
