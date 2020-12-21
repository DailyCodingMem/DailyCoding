def solution(v):
    ans = []
    p_dict = {'x' : [], 'y' : []}
    for point in v:
        p_dict['x'].append(point[0])
        p_dict['y'].append(point[1])

    for i in p_dict['x']:
        if p_dict['x'].count(i) == 1:
            ans.append(i)
    for j in p_dict['y']:
        if p_dict['y'].count(j) == 1:
            ans.append(j)
    return ans

v = [[1, 4], [3, 4], [3, 10]]
ans = []
p_dict = {'x' : [], 'y' : []}
for point in v:
    p_dict['x'].append(point[0])
    p_dict['y'].append(point[1])

for i in p_dict['x']:
    if p_dict['x'].count(i) == 1:
        ans.append(i)
for j in p_dict['y']:
    if p_dict['y'].count(j) == 1:
        ans.append(j)


