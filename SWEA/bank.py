import sys
sys.stdin = open('../inputdata/20190919-1.txt', 'r')

for test in range(int(input())):
    binary = input()
    ternary = input()
    binary_list = []
    ternary_list =[]

    for i in range(len(binary)):
        b_tmp = list(binary)
        if b_tmp[i] == '0':
            b_tmp[i] = '1'
        else:
            b_tmp[i] = '0'
        binary_list.append(int(''.join(b_tmp), 2))

    for i in range(len(ternary)):
        t_tmp = list(ternary)
        if t_tmp[i] == '0':
            t_tmp[i]='1'
            ternary_list.append(int(''.join(t_tmp), 3))
            t_tmp[i] ='2'
        elif t_tmp[i] == '1':
            t_tmp[i]='0'
            ternary_list.append(int(''.join(t_tmp), 3))
            t_tmp[i] ='2'
        else:
            t_tmp[i]='0'
            ternary_list.append(int(''.join(t_tmp), 3))
            t_tmp[i] ='1'
        ternary_list.append(int(''.join(t_tmp), 3))

    for num in binary_list:
        if num in ternary_list:
            print('#{} {}'.format(test+1, num))
            break