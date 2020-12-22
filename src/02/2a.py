import re

f = open('input.txt', mode='rt', encoding='utf-8')
mylist = f.readlines()
f.close()

correct = 0
for line in mylist:
    min_occ, max_occ, char, text = re.split('[-: ]+', line.strip())
    occ = str.count(text, char)
    if int(min_occ) <= occ <= int(max_occ):
        correct += 1

print("Answer: {}".format(correct))
