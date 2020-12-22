import itertools
import sys

# Possible optimizations:
# [ ] Use collections.deque() instead of list.append()
# [ ] Use concurrent.futures in main() to process combinations_with_length


def get_input(file):
    lines = []
    with open(file, mode='rt', encoding='utf-8') as f:
        for line in f:
            number = int(line)
            lines.append(number)

    return lines


def get_max_config(adapters):
    charging_outlet = 0
    device_adapter = adapters[-1] + 3
    minj = charging_outlet + 1
    maxj = charging_outlet + 3
    config = []
    for a in adapters:
        if minj <= a <= maxj:
            config.append(a)
            minj = a + 1
            maxj = a + 3
            if maxj == device_adapter:
                config.append(device_adapter)
                break

    return config


def get_min_config(adapters):
    device_adapter = adapters[-1] + 3
    config = [adapters[0]]
    i = 0
    while True:
        adapter = adapters[i]
        last_added = config[-1]
        if adapter < last_added:
            i = adapters.index(last_added)
            continue
        for candidate in range(adapter + 3, adapter, -1):
            if candidate in adapters:
                config.append(candidate)
                break
        if adapter + 3 == device_adapter:
            config.append(device_adapter)
            break
        i += 1

    return config


def test_config(config):
    # TODO: Implement a method that tests the validity of an adapter configuration.
    return True


def main():

    # Get all adapters
    adapters = get_input('input.txt')
    adapters.sort()

    # Get the maximum and minimum adapter configurations
    max_config = set(get_max_config(adapters))
    min_config = set(get_min_config(adapters))

    # Get the optional adapters
    diff = list(max_config - min_config)
    diff.sort()

    # Find all combinations of adapters, except max and min configs
    combinations = []  # TODO: Consider using a list comprehension here.
    for length in range(len(diff) - 1, 0, -1):  # len(diff) - 1 because the full len(diff) == max_config
        combinations_with_length = list(itertools.combinations(diff, length))  # TODO: Use multi-threading here.
        for cwl in combinations_with_length:
            combinations.append(cwl)  # TODO: Use collections.deque() here.
            if len(combinations) % 10000 == 0:
                sys.stdout.write("{}\n".format(len(combinations)))

    # Add the max and min configs too
    combinations.insert(0, tuple(max_config))
    combinations.append(tuple(min_config))
    answer = len(combinations)

    # pass
    #
    # # Get an array of bits for the optional adapters
    # selectors = [0] * len(max_config)
    # for c in diff:
    #     i = max_config.index(c)
    #     selectors[i] = 1

    # Loop through all possible combinations of selectors, starting with max_config and approaching min_config
    #    Create a configuration based on this selector combination
    #    If the config equals min_config, exit and count
    #    If not, test the configuration (we only need to test the piece that was changed)
    #        If successful, count it
    #        If not, try next

    sys.stdout.write("Answer: {}\n".format(answer))


main()

# [x] Find the adapter config using the maximum number of adapters.
# [x] Loop through 1 - length(adapters) and remove that number of adapters.
# [ ] In each config, loop through each adapter and attempt to remove it.
# [ ] If the test equals the minimun config, exit.
