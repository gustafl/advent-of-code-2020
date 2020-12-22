def get_input(file):
    with open(file, 'rt', encoding='utf8') as f:
        lines = []
        for line in f.readlines():
            line = line.strip()
            lines.append(line)
        return lines


def get_ingredients(lines):
    ingredients = set()
    for line in lines:
        pass


def main():
    lines = get_input('sample.txt')

    pass


main()
