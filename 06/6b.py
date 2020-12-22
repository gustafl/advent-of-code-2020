import re


def get_input():
    records = []
    record = ''
    with open('input.txt', mode='rt', encoding='utf-8') as f:
        for line in f:
            if line.strip():  # If line is not empty
                line = re.sub(r'\s+', ' ', line)  # Normalize whitespace on line
                record += line  # Add line to record
            else:  # If line is empty
                records.append(record.strip().split())  # Add new record
                record = ''
        if record:
            records.append(record.strip().split())  # Add the last record

    return records


def main():
    records = get_input()
    questions = 'abcdefghijklmnopqrstuvwxyz'
    total_sum = 0

    for r in records:  # Loop through records
        yes_answers = ''
        for c in questions:  # Loop through alphabet
            number_of_groups = len(r)
            number_of_yes_answers_in_group = 0
            for g in r:  # Loop through groups
                if c in g:
                    number_of_yes_answers_in_group += 1
            if number_of_yes_answers_in_group == number_of_groups:
                yes_answers += c
        total_sum += len(yes_answers)

    print(total_sum)


main()
