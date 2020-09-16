import sys
sys.setrecursionlimit(100000)
def dfs(v):
    global ans
    num_lst = list(str(v))
    # if ans != 0:
    #     return ans
    for i in num_lst:
        if int(i) == 0 or int(i) == 1:
            continue
        else:
            if v not in visited:
                v += n
                dfs(v)
                visited.append(v)
    ans.append(v)

ans = []
n = int(input())
visited = []
dfs(n)
print(max(ans))