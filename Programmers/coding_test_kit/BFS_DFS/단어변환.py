def solution(begin, target, words):
    answer = 0
    stack = [begin]
    visited = [0] * len(words)

    while stack:
        now_word = stack.pop()
        for i, next_word in enumerate(words):
            change = False
            for j in range(len(now_word)):
                if now_word[j] != next_word[j]:
                    if not change:
                        change = True
                    else:
                        break
            else:
                if visited[i] == 0:
                    stack.append(next_word)
                    visited[i] = 1
        answer += 1
        if target in stack:
            break
    if not stack:
        answer = 0

    return answer