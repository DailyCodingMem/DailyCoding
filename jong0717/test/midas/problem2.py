def solution(n, v1, v2, num, amount):
    set_list = [set([i]) for i in range(1,n+1)]

    for i in range(len(v1)):
        a, b = v1[i], v2[i]
        for tm in set_list:
            if a in tm:
                lteam = set_list.pop(set_list.index(tm))
                break
        for tm in set_list:
            if b in tm:
                rteam = set_list.pop(set_list.index(tm))
                break
        set_list.append(lteam | rteam)

    answer = {}
    for i in set_list:
        answer[min(i)] = 0

    T_dict = {}
    for i in range(len(num)):
        if num[i] in T_dict:
            T_dict[num[i]] += amount[i]
        else:
            T_dict[num[i]] = amount[i]

    for team in set_list:
        team_min = min(team)
        for t in team:
            if t in T_dict.keys():
                answer[team_min] += T_dict[t]

    for l, v in answer.items():
        if max(answer.values()) == v:
            return l

n = 10
v1 = [1, 10, 6, 5, 6, 9]
v2 = [3, 7, 2, 8, 7, 3]
num = [3, 4, 5, 1, 8, 7, 9, 2]
amount = [10, 5, 6, -6, -8, 2, -2, 5]

set_list = [set([i]) for i in range(1,n+1)]

for i in range(len(v1)):
    a, b = v1[i], v2[i]
    for tm in set_list:
        if a in tm:
            left = set_list.pop(set_list.index(tm))
            break
    for tm in set_list:
        if b in tm:
            right = set_list.pop(set_list.index(tm))
            break
    set_list.append(left | right)

answer = {}
for i in set_list:
    answer[min(i)] = 0

T_dict = {}
for i in range(len(num)):
    if num[i] in T_dict:
        T_dict[num[i]] += amount[i]
    else:
        T_dict[num[i]] = amount[i]

for team in set_list:
    team_min = min(team)
    for t in team:
        if t in T_dict.keys():
            answer[team_min] += T_dict[t]
result = []
for l, v in answer.items():
    if max(answer.values()) == v:
        result.append(l)
print(min(result))
