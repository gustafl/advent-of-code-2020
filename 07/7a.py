import re
import sys


def get_input(file):
    bags = []
    with open(file, mode='rt', encoding='utf-8') as f:
        for line in f:
            match = re.search(r'(\w+ \w+) bags contain (.*)\.', line)
            bag_name = match.group(1)
            bag_rules = re.findall(r'(\d+) (\w+ \w+) bags?', match.group(2))
            bag = (bag_name, bag_rules)
            bags.append(bag)

    return dict(bags)


def possible_bag(bags, bag, my_bag_name):
    # Get children of current bag
    bag_children = bags[bag]
    for child in bag_children:
        child_name = child[1]
        # If the child is our bag
        if child_name == my_bag_name:
            return True
        else:
            if possible_bag(bags, child_name, my_bag_name):
                return True

    return False


def main():
    bags = get_input('input.txt')
    my_bag_name = 'shiny gold'
    possible_bags = []
    for bag in bags:
        if possible_bag(bags, bag, my_bag_name):
            possible_bags.append(bag)

    for bag in possible_bags:
        sys.stdout.write("{}\n".format(bag))

    sys.stdout.write("Answer: {}\n".format(len(possible_bags)))


main()
