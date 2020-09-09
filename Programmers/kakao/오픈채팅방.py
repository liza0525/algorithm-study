# 2019 KAKAO BLIND RECRUITMENT
def solution(records):
    queries = []
    id_nickname = dict()
    answer = []

    for record in records:
        el = record.split(' ')
        queries.append([el[0], el[1]])
        if el[0] == 'Enter' or el[0] == 'Change':
            id_nickname.update({el[1]: el[2]})

    for state, ident in queries:
        if state == 'Enter':
            answer.append(id_nickname[ident]+'님이 들어왔습니다.')
        elif state == 'Leave':
            answer.append(id_nickname[ident]+'님이 나갔습니다.')

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))