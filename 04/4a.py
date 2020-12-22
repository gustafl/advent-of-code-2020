import re
import sys

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

sys.stdout.write("Total number of records: {}\n".format(len(records)))


def is_valid(rec):
    required_props = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = True

    for prop in required_props:
        if not '{}:'.format(prop) in rec:
            valid = False
            break
    return valid


valid_count = 0
for record in records:
    if is_valid(record):
        valid_count += 1

sys.stdout.write("Number of valid records: {}".format(valid_count))
