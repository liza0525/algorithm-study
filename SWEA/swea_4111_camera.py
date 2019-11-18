for test in range(int(input())):
    N, M = int(input()), int(input())
    cameras = list(map(int, input().split()))
    diffs = []

    cameras.sort()
    # print(cameras)
    if N <= M:
        print('#{} {}'.format(test+1, 0))
        continue
    for i in range(N-1):
        diffs.append(cameras[i+1] - cameras[i])

    print('#{} {}'.format(test+1, sum(sorted(diffs)[:len(diffs) - (M-1)])))