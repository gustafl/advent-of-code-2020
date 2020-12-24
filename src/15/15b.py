import timeit
from collections import deque


MAX_TURNS = 300000


def get_input(file):
    with open(file, 'rt', encoding='utf8') as f:
        return f.read().strip()


def rindex(lst, value):  # https://stackoverflow.com/a/63834895/1392152
    lst.reverse()
    i = lst.index(value)
    lst.reverse()
    return len(lst) - i - 1


def get_next_number(numbers, last_number):
    if last_number not in numbers[:-1]:
        return 0
    else:
        last_index = rindex(numbers[:-1], last_number)
        next_number = len(numbers) - 1 - last_index
        return next_number


def main():

    # Get input
    line = get_input('sample.txt')
    numbers = list(map(lambda x: int(x), line.split(',')))
    numbers = deque(numbers)

    start_time = timeit.default_timer()

    # Loop until we reach MAX_TURNS
    while len(numbers) < MAX_TURNS:
        last_number = numbers[-1]
        next_number = get_next_number(numbers, last_number)
        numbers.append(next_number)
        # if next_number > 0:
        #     numbers = numbers[next_number:]
        ln = len(numbers)
        if ln % 30000 == 0:
            print(ln)
            end_time = timeit.default_timer()
            elapsed_time = end_time - start_time
            start_time = timeit.default_timer()
            print(f"Time: {elapsed_time}")

    print(numbers[-1])


main()
