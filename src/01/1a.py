import itertools

WANTED_SUM = 2020

f = open('input.txt', mode='rt', encoding='utf-8')
mylist = f.readlines()
f.close()

for a, b in itertools.combinations(mylist, 2):
    n1, n2 = int(a), int(b)
    mysum = n1 + n2
    print("{} + {} = {}".format(n1, n2, mysum))
    if mysum == WANTED_SUM:
        answer = n1 * n2
        print("Answer: {}".format(answer))
        break
