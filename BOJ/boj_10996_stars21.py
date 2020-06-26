import sys
sys.stdin = open('../input.txt', 'r')

N = int(input())

for i in range(2*N):
    line = ''
    for j in range(N):
        if not i % 2:
            if not j % 2:
                line += '*'
            else:
                line += ' '
        else:
            if not j % 2:
                line += ' '
            else:
                line += '*'
    print(line)