import sys
from pprint import pprint
from pprint import pprint
sys.stdin = open('../inputdata/20190919-2.txt', 'r')

num = {
    '0001101': 0, '0011001': 1, '0010011': 2,
    '0111101': 3, '0100011': 4, '0110001': 5,
    '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
}

hexa_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
    '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100',
    'D': '1101', 'E': '1110', 'F': '1111'
}

for test in range(int(input())):
    n, m = map(int, input().split())
    lines = [input() for _ in range(n)]
    hexas = []
    binarys = []

    for line in lines:
        for ch in line:
            if ch != '0' and line not in hexas:
                hexas.append(line)

    for hexa in hexas:
        tmp =''
        for i in range(len(hexa)):
            tmp += hexa_to_bin[hexa[i]]
        binarys.append(tmp.rstrip('0'))

    print(binarys)

