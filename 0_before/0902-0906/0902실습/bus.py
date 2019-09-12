import sys
sys.stdin = open('bus.txt', 'r')

for test in range(int(input())):
    n = int(input())
    buses = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())
    stops = dict()
    for _ in range(p):
        stops.update({int(input()): 0})

    for k in stops.keys():
        for bus in buses:
            if bus[0] <= k <= bus[1]:
                stops[k] += 1
    print('#{} {}'.format(test + 1, ' '.join(map(str, stops.values()))))