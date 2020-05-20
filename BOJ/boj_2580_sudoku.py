import sys
sys.stdin = open('../input.txt', 'r')

sudoku = [list(map(int, input().split())) for _ in range(9)]