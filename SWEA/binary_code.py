num = {
    '0001101': 0, '0011001': 1, '0010011': 2,
    '0111101': 3, '0100011': 4, '0110001': 5,
    '0101111': 6, '0111011': 7, '0110111': 8,'0001011': 9
}
 
for test in range(int(input())):
    n, m = map(int, input().split())
    lines = [input() for _ in range(n)]
    code = []
    res = 0
    for line in lines:
        if '1' in line:
            tmp = line
            break
    for i in range(len(tmp)-7):
        if tmp[i:i+7] in num.keys() and tmp[i+7:i+14] in num.keys():
            binary_code = tmp[i:i+56]
            break
             
    for i in range(0, len(binary_code)-6, 7):
        code.append(num[binary_code[i:i+7]])
 
 
    if (sum(code[::2]) * 3 + sum(code[1::2])) % 10 == 0:
        res = sum(code)
 
    print('#{} {}'.format(test+1, res))
