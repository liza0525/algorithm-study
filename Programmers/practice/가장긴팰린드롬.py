def solution(s):
    answer = 0
    def palin(substring):
        for i in range(len(substring) // 2):
            if substring[i] != substring[len(substring)-i-1]:
                return False
        else:
            return True


    for i in range(len(s)):
        for j in range(len(s), 0, -1):
            if j < i: continue
            if j - i < answer: continue
            substring = s[i:j]
            if palin(substring):
                answer = len(substring)


    return answer

print(solution('abcdcba'))
print(solution('abacde'))