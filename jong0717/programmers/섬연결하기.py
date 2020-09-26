def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    visited = [0] * n
    visited[0] = 1
    while sum(visited) != n :
        for cost in costs:
            a, b, c = cost
            if visited[a] or visited[b]:
                if visited[a] and visited[b]:
                    continue
                else:
                    visited[a] = 1
                    visited[b] = 1
                    answer += c
                    break
    return answer
# n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(costs.sort(key=lambda x:x[2]))
# print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))