import sys


def get_input(file):
    lines = []
    with open(file, mode='rt', encoding='utf-8') as f:
        i = 0
        for line in f:
            command = line.split()[0]
            argument = int(line.split()[1].strip())
            line = (command, argument, False, i)
            lines.append(line)
            i += 1

    return lines


def try_run(lines):
    accumulator = 0
    success = False
    i = 0

    while True:
        if i >= len(lines):
            success = True
            break

        line = lines[i]
        command = line[0]
        argument = int(line[1])
        passed = line[2]

        if passed:
            # sys.stdout.write("We've already been on line {} ({} {}). Quitting.\n"
            #                  .format(i, command, argument))
            return False  # If we've already been here, exit the loop

        if command == 'nop':
            # sys.stdout.write("On line {} ({} {}): Did nothing. Moving to line {}.\n"
            #                  .format(i, command, argument, i + 1))
            lines[i] = (command, argument, True, i)
            i += 1
        elif command == 'acc':
            accumulator += argument
            # sys.stdout.write("On line {} ({} {}): Changed accumulator by {} to {}. Moving to line {}.\n"
            #                  .format(i, command, argument, argument, accumulator, i + 1))
            lines[i] = (command, argument, True, i)
            i += 1
        elif command == 'jmp':
            # sys.stdout.write("On line {} ({} {}): Jumping {} lines to line {}.\n"
            #                  .format(i, command, argument, argument, i + argument))
            lines[i] = (command, argument, True, i)
            i += argument

    if success:
        sys.stdout.write("Answer: {}\n".format(accumulator))
        return True


def hack_input(original_lines, mylist):
    for line in mylist:
        lines = original_lines.copy()
        argument = int(line[1])
        visited = line[2]
        index = int(line[3])
        updated_line = ('nop', argument, visited, index)
        lines[index] = updated_line
        if try_run(lines):
            return True

    return False


def main():

    # Read input file
    original_lines = get_input('input.txt')

    # Get all 'jmp' and 'nop' command lines
    jmps = list(filter(lambda ln: ln[0] == 'jmp', original_lines))
    # Avoid 'nop' lines where the argument is 0 to avoid creating lines with 'jmp +0' (infinite loop)
    nops = list(filter(lambda ln: ln[0] == 'nop' and not ln[1] == 0, original_lines))

    # Make all possible modifications until we succeed
    sys.stdout.write("Total lines: {}\n".format(len(original_lines)))
    sys.stdout.write("{} 'nop' -> 'jmp'\n".format(len(nops)))
    if hack_input(original_lines, nops):
        return
    sys.stdout.write("{} 'jmp' -> 'nop'\n".format(len(jmps)))
    if hack_input(original_lines, jmps):
        return


main()
