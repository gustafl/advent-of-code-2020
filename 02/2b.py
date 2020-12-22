import re

f = open('input.txt', mode='rt', encoding='utf-8')
mylist = f.readlines()
f.close()

correct = 0
for line in mylist:
    pos_1, pos_2, char, text = re.split('[-: ]+', line.strip())
    pos_1 = int(pos_1) - 1
    pos_2 = int(pos_2) - 1
    if (text[pos_1] == char) ^ (text[pos_2] == char):
        correct += 1

print("Answer: {}".format(correct))
