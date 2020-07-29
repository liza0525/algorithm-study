def solution(tickets):
    paths = []
    tdict = dict()

    for ticket in tickets:
        if ticket[0] not in tdict.keys():
            tdict.update({ticket[0]: [ticket[1]]})
        else:
            tdict[ticket[0]].append(ticket[1])

    for k in tdict.keys():
        tdict[k].sort(reverse=True)

    stack = ['ICN']

    while stack:
        dep = stack[-1]
        if dep not in tdict or len(tdict[dep]) == 0: # 해당 출발지에서 더 이상 갈 곳이 없는 경우
            paths.append(stack.pop())
        else: # 갈 곳이 있을 때
            stack.append(tdict[dep][-1])
            tdict[dep].pop()

    return paths[::-1]

# print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))
# print(solution([['ICN', 'A'], ['A', 'B'], ['B', 'A'], ['A', 'ICN'], ['ICN', 'A']]))
print(solution([['ICN', 'A'], ['ICN', 'B'], ['B', 'ICN']]))