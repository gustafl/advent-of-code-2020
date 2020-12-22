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


def get_number_of_descendants(bags, bag):
    # Count the amount of this type of bag
    bag_count = int(bag[0])
    bag_name = bag[1]
    # Get children of current bag
    bag_children = bags[bag_name]
    for child in bag_children:
        child_amount = int(child[0])
        child_name = child[1]
        # If the child is our bag
        decendant_count = get_number_of_descendants(bags, child)
        bag_count += decendant_count

    return bag_count


def main():
    bags = get_input('sample.txt')
    my_bag_name = 'shiny gold'
    my_bag = bags[my_bag_name]
    count = 0
    for bag in my_bag:
        count += get_number_of_descendants(bags, bag)

    sys.stdout.write("Answer: {}\n".format(count))


main()

# Not: 31
# Not: 15
