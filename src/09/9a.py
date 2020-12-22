import itertools
import sys


def get_input(file):
    lines = []
    with open(file, mode='rt', encoding='utf-8') as f:
        for line in f:
            number = int(line)
            lines.append(number)

    return lines


def main():
    lines = get_input('input.txt')
    answer = 0
    offset = 25
    preamble_start = 0
    preamble = lines[preamble_start:preamble_start+offset]
    for i in range(offset, len(lines) - offset):
        number = lines[i]
        valid = False
        for a, b in itertools.combinations(preamble, 2):
            if a + b == number:
                valid = True
                break
        if not valid:
            answer = number
            break
        preamble_start += 1
        preamble = lines[preamble_start:preamble_start+offset]

    sys.stdout.write("Answer: {}\n".format(answer))


main()
