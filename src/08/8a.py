import sys


def get_input(file):
    lines = []
    with open(file, mode='rt', encoding='utf-8') as f:
        for line in f:
            command = line.split()[0]
            argument = int(line.split()[1].strip())
            line = (command, argument, False)
            lines.append(line)

    return lines


def main():
    lines = get_input('input.txt')
    accumulator = 0
    i = 0

    while True:
        line = lines[i]
        command = line[0]
        argument = int(line[1])
        passed = line[2]

        if passed:
            sys.stdout.write("We've already been on line {} ({} {}). Quitting.\n"
                             .format(i, command, argument))
            break  # If we've already been here, exit the loop

        if command == 'nop':
            sys.stdout.write("On line {} ({} {}): Did nothing. Moving to line {}.\n"
                             .format(i, command, argument, i + 1))
            lines[i] = (command, argument, True)
            i += 1
        elif command == 'acc':
            accumulator += argument
            next_line = i + 1
            sys.stdout.write("On line {} ({} {}): Changed accumulator by {} to {}. Moving to line {}.\n"
                             .format(i, command, argument, argument, accumulator, i + 1))
            lines[i] = (command, argument, True)
            i += 1
        elif command == 'jmp':
            sys.stdout.write("On line {} ({} {}): Jumping {} lines to line {}.\n"
                             .format(i, command, argument, argument, i + argument))
            lines[i] = (command, argument, True)
            i += argument

    sys.stdout.write("Answer: {}\n".format(accumulator))


main()
