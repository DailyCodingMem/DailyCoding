def solution(N, stages):
    answer = []
    l_stage = len(stages)
    for i in range(1,N+1):
        if i in stages:
            answer.append((i, (stages.count(i) / l_stage)))
            l_stage -= stages.count(i)
        else:
            answer.append((i,0))
    result = []
    for idx, val in sorted(answer, key=lambda ans: ans[1], reverse=True):
        result.append(idx)

    return result
