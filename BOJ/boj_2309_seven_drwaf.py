import sys
sys.stdin = open('../input.txt', 'r')

def solve(d, next):
    global real
    if d == 7:
        if sum(real) == 100:
            print('\n'.join(map(str, sorted(real))))
            sys.exit(0)
    else:
        for i in range(next, 9):
            if sum(real) <= 100:
                real.append(heights[i])
                solve(d+1, next+1)
                real.pop()


heights = [int(input()) for _ in range(9)]
real = []

solve(0, 0)