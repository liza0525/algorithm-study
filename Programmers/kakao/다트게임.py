# 2018 KAKAO BLIND RECRUITMENT
def solution(dart_result):
    info = []
    res = []

    for i in range(len(dart_result)):
        if dart_result[i] == '1':
            if dart_result[i+1] == '0':
                info.append(10)
            else:
                info.append(1)
        elif dart_result[i] == '0':
            if dart_result[i-1] == '1':
                continue
            else:
                info.append(0)
        else:
            if dart_result[i].isdigit():
                info.append(int(dart_result[i]))
            else:
                info.append(dart_result[i])

    i = 0
    while i < len(info)-1:
        if info[i+1] == 'S':
            temp = info[i]
        elif info[i+1] == 'D':
            temp = info[i] ** 2
        elif info[i+1] == 'T':
            temp = info[i] ** 3

        if i < len(info) - 2:
            if info[i+2] == '#':
                temp *= (-1)
                i += 1
            elif info[i+2] == '*':
                if res:
                    res[-1] *= 2
                temp *= 2
                i += 1
        res.append(temp)
        i += 2
    return sum(res)


print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))