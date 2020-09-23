from copy import deepcopy
def solution(str1, str2):
    set1 = []
    set2 = []
    alpha = list('ABCDEFGHIJKLMNOPQRSTUVWYZabcdefghijklmnopqrstuvwxyz')
    for i in range(len(str1)-1): # 0 1 2 3 4 5
        if str1[i] in alpha and str1[i+1] in alpha:
            set1.append((str1[i]+str1[i+1]).lower())
    for i in range(len(str2)-1): # 0 1 2 3 4 5
        if str2[i] in alpha and str2[i + 1] in alpha:
            set2.append((str2[i]+str2[i+1]).lower())
    and_set = []
    or_set = []
    temp_set1 = deepcopy(set1)
    temp_set2 = deepcopy(set2)

    k = 0
    visited = []
    for i in temp_set1: # set1 집합 원소를 돌면서
        if i in temp_set2: # 같은 게 있으면
            if i not in visited:
                visited.append(i)
                k += min(temp_set1.count(i), temp_set2.count(i))
    for i in set1: # 먼저 첫번째 거 다 넣어 놓고
        or_set.append(i)
    for j in set2: # 두번째 거 돌면서
        if or_set.count(j) < set2.count(j):
            or_set.append(j)
    if len(and_set) == 0 and len(or_set) == 0:
        J = 1
    else:
        J = k / len(or_set)

    JACA = int(J * 65536)
    return JACA