import sys
from pprint import pprint
sys.stdin = open('read_column.txt', 'r')

for test in range(int(input())):
    data = [[ch for ch in input()] for _ in range(5)]
    maxlen = max([len(data[i]) for i in range(len(data))])
    res = []
    for i in range(5):
        tmp = [None] * maxlen
        for j in range(len(data[i])):
            tmp[j] = data[i][j]
        data[i] = tmp
    data = list(map(list, zip(*data)))

    res = ''
    for i in range(maxlen):
        for j in range(5):
            if data[i][j]:
                res += data[i][j]
    print('#{} {}'.format(test+1, res))