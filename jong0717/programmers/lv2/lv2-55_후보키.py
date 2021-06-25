
from itertools import combinations as combs
def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])

    candidates = []
    for i in range(1, n_col+1):
        # extend는 iterable의 각 항목을 넣는다.
        candidates.extend(combs(range(n_col),i))

    final = []
    for keys in candidates:
        tmp = [tuple([item[key] for key in keys]) for item in relation]
        if len(set(tmp)) == n_row:
            final.append(keys)

    answer = set(final)
    for i in range(len(final)):
        for j in range(i+1, len(final)):
            # intersection을 이용해서 최소성을 만족하는지 확인
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                # discard는 제거할 것이 없어도 실행 가능. remove와 차이점
                answer.discard(final[j])
    return len(answer)

