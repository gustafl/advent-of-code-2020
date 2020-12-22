import itertools

WANTED_SUM = 2020

f = open('input.txt', mode='rt', encoding='utf-8')
mylist = f.readlines()
f.close()

for a, b, c in itertools.combinations(mylist, 3):
    n1, n2, n3 = int(a), int(b), int(c)
    mysum = n1 + n2 + n3
    print("{} + {} + {} = {}".format(n1, n2, n3, mysum))
    if mysum == WANTED_SUM:
        answer = n1 * n2 * n3
        print("Answer: {}".format(answer))
        break
