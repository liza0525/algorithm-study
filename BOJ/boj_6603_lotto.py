import sys
sys.stdin = open('../input.txt', 'r')

data = []
while True:
    now_input = input()
    if now_input == '0':
        break
    data.append(list(now_input.split()))
