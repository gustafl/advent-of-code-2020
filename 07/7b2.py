import re
import sys


class Bag:

    def __init__(self, name):
        self._name = name
        self._parent = None
        self._children = []

    def get_name(self):
        return self._name

    def get_parent(self):
        return self._parent

    def set_parent(self, parent):
        self._parent = parent

    def get_children(self):
        return self._children

    def set_children(self, children):
        self._children = children

    def add_child(self, child):
        if child not in self._children:
            self._children.append(child)


def get_input(file):
    bags = []
    with open(file, mode='rt', encoding='utf-8') as f:
        for line in f:
            match = re.search(r'(\w+ \w+) bags contain (.*)\.', line)
            bag_name = match.group(1)
            bag_rules = re.findall(r'(\d+) (\w+ \w+) bags?', match.group(2))
            bag = (bag_name, bag_rules)
            bags.append(bag)

    # TODO: Find out if it's possible in Python to convert amounts to integers here already.

    return dict(bags)


def build_tree(bags, bag):
    name = bag.get_name()
    children = bags[name]
    for child in children:
        child_bag_amount = int(child[0])
        child_bag_name = child[1]
        for i in range(0, child_bag_amount):
            child_bag = Bag(child_bag_name)
            child_bag.set_parent(bag)
            bag.add_child(child_bag)
            build_tree(bags, child_bag)


def count_bags(bag):
    children = bag.get_children()
    total = 0
    for child in children:
        total += count_bags(child)
    return 1 + total


def print_tree(bag, indents):
    indent = " " * indents
    sys.stdout.write("{}{}\n".format(indent, bag.get_name()))
    children = bag.get_children()
    for child in children:
        print_tree(child, indents + 4)


def main():
    bags = get_input('input.txt')
    bag = Bag('shiny gold')

    # Build the tree
    build_tree(bags, bag)

    # Count bags
    answer = count_bags(bag) - 1

    # Print bags
    print_tree(bag, 0)
    
    sys.stdout.write("Answer: {}\n".format(answer))


main()
