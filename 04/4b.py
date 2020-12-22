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
        if prop == 'byr':  # Four digits; at least 1920 and at most 2002.
            match = re.search(r'byr:(\d{4})( |$)', rec)
            if match:
                year = int(match.group(1))
                if year < 1920 or year > 2002:
                    valid = False
                    break
            else:
                valid = False
                break
        elif prop == 'iyr':  # Four digits; at least 2010 and at most 2020.
            match = re.search(r'iyr:(\d{4})( |$)', rec)
            if match:
                year = int(match.group(1))
                if year < 2010 or year > 2020:
                    valid = False
                    break
            else:
                valid = False
                break
        elif prop == 'eyr':  # Four digits; at least 2020 and at most 2030.
            match = re.search(r'eyr:(\d{4})( |$)', rec)
            if match:
                year = int(match.group(1))
                if year < 2020 or year > 2030:
                    valid = False
                    break
            else:
                valid = False
                break
        elif prop == 'hgt':  # a number followed by either cm or in:
            # If cm, the number must be at least 150 and at most 193.
            # If in, the number must be at least 59 and at most 76.
            match = re.search(r'hgt:(\d+)(cm|in)( |$)', rec)
            if match:
                height = int(match.group(1))
                unit = match.group(2)
                if (unit == 'cm' and (height < 150 or height > 193)) or (unit == 'in' and (height < 59 or height > 76)):
                    valid = False
                    break
            else:
                valid = False
                break
        elif prop == 'hcl':  # A # followed by exactly six characters 0-9 or a-f.
            match = re.search(r'hcl:(#[0-9a-f]{6})( |$)', rec)
            if not match:
                valid = False
                break
        elif prop == 'ecl':  # Exactly one of: amb blu brn gry grn hzl oth.
            match = re.search(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)( |$)', rec)
            if not match:
                valid = False
                break
        elif prop == 'pid':  # A nine-digit number, including leading zeroes.
            match = re.search(r'pid:(\d{9})( |$)', rec)
            if not match:
                valid = False
                break

    return valid


valid_count = 0
for record in records:
    if is_valid(record):
        valid_count += 1

sys.stdout.write("Number of valid records: {}".format(valid_count))
