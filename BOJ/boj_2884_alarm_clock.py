import sys
sys.stdin = open('../input.txt', 'r')

hour, minute = map(int, input().split())

if minute < 45:
    if hour != 0:
        hour -= 1
    else:
        hour = 23
minute += 15
if minute >= 60:
    minute -= 60

print(hour, minute)