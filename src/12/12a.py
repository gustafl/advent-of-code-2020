import sys


def get_input(file):
    with open(file, 'rt', encoding='utf8') as f:
        lines = []
        for line in f.readlines():
            line = line.strip()
            lines.append(line)
        return lines


def main():
    lines = get_input('input.txt')
    position = [0, 0]  # East, North
    direction = 90  # East
    count = 1
    for change in lines:
        command = change[0:1]
        units = int(change[1:])
        if command == "E" or (command == "F" and direction == 90):
            position[0] += units
            sys.stdout.write("{}. Move east {} units. New position: {}\n".format(count, units, position))
        elif command == "W" or (command == "F" and direction == 270):
            position[0] -= units
            sys.stdout.write("{}. Move west {} units. New position: {}\n".format(count, units, position))
        elif command == "N" or (command == "F" and direction == 0):
            position[1] += units
            sys.stdout.write("{}. Move north {} units. New position: {}\n".format(count, units, position))
        elif command == "S" or (command == "F" and direction == 180):
            position[1] -= units
            sys.stdout.write("{}. Move south {} units. New position: {}\n".format(count, units, position))
        elif command == "L":
            direction -= units
            if direction < 0:
                direction += 360
            sys.stdout.write("{}. Turn left {} units. New position: {}\n".format(count, units, position))
        elif command == "R":
            direction += units
            if direction > 360:
                direction -= 360
            sys.stdout.write("{}. Turn right {} units. New position: {}\n".format(count, units, position))
        count += 1

    ew = abs(position[0])
    ns = abs(position[1])
    answer = ew + ns
    sys.stdout.write("Answer: {}\n".format(answer))


main()

# Not: 3251 (too high)
# The sample works, but not the input.
