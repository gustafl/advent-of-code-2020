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
    adapters = get_input('sample.txt')
    adapters.sort()

    charging_outlet = 0
    device_adapter = adapters[-1] + 3
    minj = charging_outlet + 1
    maxj = charging_outlet + 3
    diff_1 = []
    diff_3 = []
    prev = charging_outlet
    for a in adapters:
        if minj <= a <= maxj:
            sys.stdout.write("Adapter {} may be used.\n".format(a))
            diff = a - prev
            prev = a
            if diff == 1:
                diff_1.append(a)
            elif diff == 3:
                diff_3.append(a)
            minj = a + 1
            maxj = a + 3
            if maxj == device_adapter:
                diff_3.append(maxj)
                break

    diff_1_len = len(diff_1)
    diff_3_len = len(diff_3)
    answer = diff_1_len * diff_3_len
    sys.stdout.write("Answer: {}\n".format(answer))


main()
