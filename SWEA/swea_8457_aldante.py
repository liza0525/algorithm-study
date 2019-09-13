import sys
sys.stdin = open('aldante.txt', 'r')

for test in range(int(input())):
    n, b, e = map(int, input().split())
    sandtimers = list(map(int, input().split()))
    res = 0
    for sandtimer in sandtimers:
        t = 1
        while True:
            if sandtimer*t < b-e:
                t += 1
            elif b-e <= sandtimer*t <= b+e:
                res += 1
                break
            elif sandtimer*t > b+e:
                break
    print('#{} {}'.format(test+1, res))