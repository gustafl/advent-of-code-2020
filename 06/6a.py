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
                records.append(record.strip())  # Add new record
                record = ''
        if record:
            records.append(record.strip())  # Add the last record

    return records


def main():
    records = get_input()
    questions = 'abcdefghijklmnopqrstuvwxyz'
    total_sum = 0

    for r in records:
        yes_answers = ''
        for c in questions:
            if c in r and c not in yes_answers:
                yes_answers += c
        total_sum += len(yes_answers)

    print(total_sum)


main()
