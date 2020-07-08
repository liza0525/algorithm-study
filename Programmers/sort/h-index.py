def solution(citations):
    for h in range(len(citations)+1, -1, -1):
        higher_h = 0
        for c in citations:
            if c >= h:
                higher_h +=1
        if higher_h >= h:
            return h