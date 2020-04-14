import sys
sys.stdin = open('../input.txt', 'r')


def combi(arr, d, next):
    if d == 6:
        print(' '.join(map(str, arr)))
    else:
        for i in range(next, len(data)):
            if data[i] not in arr and sorted(arr + [data[i]]) not in memo:
                arr.append(data[i])
                memo.append(sorted(arr))
                combi(arr, d+1, next+1)
                arr.pop()


data_list = []
while True:
    now_input = input()
    if now_input == '0':
        break
    data_list.append(list(map(int, now_input.split())))

for data in data_list:
    memo = []
    N = data.pop(0)
    combi([], 0, 0)
    if data != data_list[-1]:
        print()
