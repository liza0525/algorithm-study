from math import sqrt


def solution(brown, yellow):
    for row in range(1, int(sqrt(yellow))+1):
        if not yellow % row:
            col = yellow // row
            if row * 2 + col * 2 + 4 == brown:
                return [col+2, row+2]