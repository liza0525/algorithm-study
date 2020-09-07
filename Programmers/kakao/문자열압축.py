# 2020 KAKAO BLIND RECRUITMENT
def solution(s):
    min_len = 1001
    if len(s) == 1:
        return 1
    for cut_len in range(1, len(s) // 2 + 1): # 최대 압축 길이는 s 길이의 절반
        cnt, idx = 0, 0 # cnt : 현재 문자열이 반복되는 횟수, idx : 현재 idx 위치
        cut_word, new_s = '', '' # cut_word : 현재 반복되는 문자열, new_s : 압축된 문자열
        while idx < len(s): # 문자열 압축하기
            cut_word = s[idx:idx + cut_len]
            while True: # 해당 문자열이 몇 번 반복되는지
                if s[idx:idx + cut_len] == cut_word: # 반복 될 때
                    cnt += 1
                    idx += cut_len
                else: # 반복이 되지 않을 때
                    if cnt != 0: # 카운팅이 된 경우는 지금까지의 문자열 저장 후 새로 문자열을 잘라줘야 함
                        if cnt != 1:
                            new_s += str(cnt)
                        new_s += cut_word
                        cnt = 0
                    elif cnt == 0: # 카운팅이 안 된 경우에는 아예 반복자체가 안된 경우
                        new_s += s[idx]
                        idx += 1
                    break
        if len(new_s) < min_len:
            min_len = len(new_s)
    return min_len


print(solution('aabbaccc'))
print(solution('ababcdcdababcdcd'))
print(solution('abcabcdede'))
print(solution('abcabcabcabcdededededede'))
print(solution('xababcdcdababcdcd'))
# Edge Case
print(solution('a'))