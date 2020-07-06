def solution(genres, plays):
    answer = []
    musics = dict()
    total_time = dict()
    for idx, time in enumerate(plays):
        if genres[idx] not in musics:
            musics[genres[idx]] = [(idx, time)]
        else:
            musics[genres[idx]].append((idx, time))
        if genres[idx] not in total_time:
            total_time[genres[idx]] = time
        else:
            total_time[genres[idx]] += time

    total_time = sorted(total_time.items(), key=lambda x: -x[1])

    for g, tt in total_time:
        mlist = sorted(musics[g], key=lambda x: (-x[1], x[0]))
        answer.append(mlist[0][0])
        if len(mlist) > 1:
            answer.append(mlist[1][0])

    return answer