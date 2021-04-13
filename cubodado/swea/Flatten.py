for t in range(10):
    limit = int(input())
    height = list(map(int, input().split()))
    for i in range(limit, 0, -1):
        max_n = height.index(max(h))
        min_n = height.index(min(h))
        height[max_n] -= 1
        height[min_n] += 1
 
    print("#%d %d" % (t+1, max(h)-min(h)))