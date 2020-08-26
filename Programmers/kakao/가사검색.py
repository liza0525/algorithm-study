# 2020 KAKAO BLIND RECRUITMENT
def solution(words, queries):
    answer = []
    for query in queries:
        cnt = 0
        start, end = 0, len(query)
        if query[0] == '?':
            for i in range(1, len(query)):
                if query[i] != '?':
                    start = i
                    break
        elif query[-1] == '?':
            for i in range(len(query)-2, -1, -1):
                if query[i] != '?':
                    end = i+1
                    break
        for word in words:
            if len(query) != len(word): continue
            for i in range(start, end):
                if query[i] != word[i]: break
            else:
                cnt += 1
        answer.append(cnt)
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))