import sys
sys.stdin = open('../input.txt', 'r')


# class Queue():
#     def __init__(self):
#         self.lst = list()
#
#     def insert(self, x):
#         self.lst.append(x)
#
#     def pop(self):
#         # print(self.lst[0])
#         self.lst = self.lst[1:]
#
#     def size(self):
#         print(len(self.lst))
#
#     def first(self):
#         print(self.lst[0])
#
#     def last(self):
#         print(self.lst[-1])


tc = int(input())
for _ in range(tc):
    N, M = map(int, sys.stdin.readline().split())
    importance = list(map(int, sys.stdin.readline().split()))
    q = list()
    for i in range(N):
        q.append([importance[i], i]) # 문서 중요도, 문서 번호

    res = 0
    while True:
        if q[0][0] == max(q)[0]:
            impt, num = q.pop(0)
            res += 1
            if num == M:
                print(res)
                break
        else:
            q.append(q.pop(0))