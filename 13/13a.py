import sys
import itertools


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
    result.sort()
    return result


def get_schedule(bus, departure):
    schedule = []
    for i in range(0, departure, bus):
        schedule.append(i)
        i += bus

    next_bus = schedule[-1] + bus
    schedule.append(next_bus)
    return schedule


def get_earliest_bus(schedules, departure):
    earliest_time = 0
    earliest_bus = 0
    for schedule in schedules:
        first = departure
        last = schedule[-1]
        for i in range(first, last + 1):
            if i in schedule:
                if earliest_time == 0 or i < earliest_time:
                    earliest_bus = schedule[1]  # The second element of the schedule, which equals the bus number
                    earliest_time = i
    return earliest_bus, earliest_time


def main():
    lines = get_input('input.txt')
    departure = int(lines[0])  # My earliest departure time
    buses = lines[1].split(',')  # Today's available buses
    buses = filter_buses(buses)  # Clean up the list of buses

    sys.stdout.write("My earliest departure: {}\n".format(departure))
    sys.stdout.write("Today's available buses: {}\n\n".format(buses))

    # Get bus schedules
    schedules = []
    for bus in buses:
        schedule = get_schedule(bus, departure)
        schedules.append(schedule)

    # Loop through schedules to find the earliest bus after my earliest departure time
    earliest_bus, earliest_time = get_earliest_bus(schedules, departure)
    sys.stdout.write("The earliest bus is: {}\n".format(earliest_bus))
    sys.stdout.write("It departs at: {}\n\n".format(earliest_time))
    wait_time = earliest_time - departure
    answer = earliest_bus * wait_time
    sys.stdout.write("Answer: {}\n".format(answer))


main()
