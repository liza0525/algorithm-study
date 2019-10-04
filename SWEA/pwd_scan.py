import sys
sys.stdin = open('../inputdata/20190919-2.txt', 'r')
#
# num = {
#     '0001101': 0, '0011001': 1, '0010011': 2,
#     '0111101': 3, '0100011': 4, '0110001': 5,
#     '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
# }
# #
# # hexadecimal = {
# #     '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
# #     '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100',
# #     'D': '1101', 'E': '1110', 'F': '1111'
# # }
#
# for test in range(int(input())):
#     n, m = map(int, input().split())
#     lines = [input() for _ in range(n)]
#
#     # code = ''
#     # pressed_code = ''
#     # include_codes = []
#     # real_hexa = []
#     # pressed_codes = []
#     # codes = []
#     # code_list = []
#     # res = 0
#     # code_num =[]
#     #
#     # for line in lines:
#     #     for i in range(m):
#     #         if line[i] != '0' and line[i] in hexadecimal and line not in include_codes:
#     #             include_codes.append(line)
#     #
#     # print('#'+str(test+1))
#     # print(include_codes)
#     #
#     # for include_code in include_codes:
#     #     i = 1
#     #     while True:
#     #         if include_code[i] != '0':
#     #             for j in range(i+1, len(include_code)-i):
#     #                 if include_code[j] != '0':
#     #                     real_hexa.append(include_code[i:j])
#     #                     i += len(real_hexa[-1])
#     #                     break
#     #         else:
#     #             i += 1
#     # print(real_hexa)
#
#
#     #
#     # for include_code in include_codes:
#     #     for i in range(len(include_code)):
#     #         if include_code[i] != '0':
#     #             code += hexadecimal[include_code[i]]
#     #     codes.append(code)
#     # print(codes)
#     # print('='*50)
#     #
#     # for code in codes:
#     #     print(code)
#     #     for i in range(len(code)-1, -1, -1):
#     #         if code[i] == '1':
#     #             j = 1
#     #             while i-56*j-1 >= 0:
#     #                 tmp = ''
#     #                 for k in range(i, i-6*j-1, -j):
#     #                     tmp += code[k]
#     #                 tmp = tmp[::-1]
#     #                 if tmp in num.keys():
#     #                     code = code[i-56*j+1:i+1]
#     #                     break
#     #                 else:
#     #                     j += 1
#     #                 # pressed_code += code[::j]
#     #             pressed_codes.append(code[::j])
#     #             break
#     #
#     # print(pressed_codes)
#     # for pressed_code in pressed_codes:
#     #     for i in range(0, len(pressed_code), 7):
#     #         code_num.append(num[pressed_code[i:i+7]])
#     #         print(code_num)
#     #     code_list.append(code_num)
#     # print(code_list)
#     # for code in code_list:
#     #     if (sum(code[::2]) * 3 + sum(code[1::2])) % 10 == 0:
#     #         res = sum(code)
#     #
#     # print('#{} {}'.format(test+1, res))

num = {'0001101': 0, '0011001': 1, '0010011': 2,
       '0111101': 3, '0100011': 4, '0110001': 5,
       '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
}

hexa_to_binary = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
}

for test in range(int(input())):
    n, m = map(int, input().split())
    lines = [input() for _ in range(n)]
    codelines = []
    codes = []
    results = []

    for line in lines:
        tmp = ''
        for ch in line:
            tmp += hexa_to_binary[ch]
        tmp_rst = tmp.rstrip('0')
        if tmp_rst and tmp_rst not in codelines:
            codelines.append(tmp_rst)
    print(codelines)
    for codeline in codelines:
        i = len(codeline)-1
        while i >= 0:
            j = 1
            while i-56*j >= 0:
                if codeline[i-7*j+1:i+1:j] in num.keys():
                    if codeline[i-56*j+1:i+1:j] not in codes:
                        codes.append(codeline[i-56*j+1:i+1:j])
                    i = i-56*j+1
                    codeline = codeline[:i]
                    j = 1
                    break
                else:
                    j += 1
            i -= 1

    print(codes)

    for code in codes:
        tmp = []
        for i in range(0, 56, 7):
            # if code[i:i+7] in num.keys():
            tmp.append(num[code[i:i+7]])
        results.append(tmp)
    res = 0

    for result in results:
        if (sum(result[::2]*3 + result[1::2]) % 10) == 0:
            res += sum(result)
    print('#{} {}'.format(test+1, res))