import sys
sys.stdin = open('../input.txt', 'r')

while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A+B)
    except:
        break
