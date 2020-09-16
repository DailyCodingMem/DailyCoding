from collections import deque
n = int(input())
num_lst = list(input())
ans = deque()
cnt = 0
for i in range(n-1, -1, -1):
    if cnt == 3:
        ans.appendleft(',')
        cnt = 0
    ans.appendleft(num_lst[i])
    cnt += 1

print(''.join(ans))