import sys
import multiprocessing
import time


def get_input(file):
    with open(file, 'rt', encoding='utf8') as f:
        lines = []
        for line in f.readlines():
            line = line.strip()
            lines.append(line)
        return lines


def filter_buses(buses):
    result = []
    for bus in buses:
        if bus != 'x':
            result.append(int(bus))
        else:
            result.append(-1)
    return result


BATCH_SIZE = 1000


def do_work(start):
    start_time = time.time()
    t = start
    answer = -1
    while True:

        if t >= t + BATCH_SIZE:
            break

        # Loop through buses by position
        for position in range(1, len(buses)):
            bus = buses[position]  # Bus ID and departure interval

            if bus == -1:  # Bus is not available
                continue

            comp = t + position
            if comp % bus != 0:  # If bus n doesn't depart on the right time, try bus 0's next departure
                break

            if bus == buses[-1]:  # If this is the last bus in the list
                answer = t  # Success!
                break

        if answer:  # If we found an answer, break
            break

        t += buses[0]

    end_time = time.time()
    print(f'\nBatch completed in {end_time - start_time}\n')
    return answer


def main():
    lines = get_input('sample.txt')
    buses = lines[1].split(',')  # Today's available buses
    buses = filter_buses(buses)  # Clean up the list of buses

    sys.stdout.write("Today's available buses: {}\n\n".format(buses))

    # Set up multiprocessing pool
    pool = multiprocessing.Pool()
    result = pool.map(do_work(start), buses)

    start = 0
    while True:
        answer = do_work(buses, start)
        start += BATCH_SIZE
        if answer > 0:
            sys.stdout.write("Answer: {}\n".format(answer))
            break


main()

# Work in progress.
