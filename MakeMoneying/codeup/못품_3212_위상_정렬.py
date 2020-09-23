from collections import defaultdict
v,m = map(int,input().split())
# v,m = 6,8
my_dict = {}
for i in range(m):
    A,B = map(int,input().split())
    if not A in my_dict:
        my_dict[A] = [B]
    else:
        my_dict[A].append(B)

# my_dict = {1: [2], 2: [3, 4], 3: [4, 6], 4: [5, 6], 5: [6]}

visited = [True] * (v+1)

def put_basket(point):
    global flag
    basket = []
    visited[point] = False
    if point in my_dict:
        for apl in my_dict[point]:
            if visited[apl]:
                basket.append(apl)
        
        
        for bug in basket:
            put_basket(bug)
            if flag:
                return
        trace.append(point)

        basket.sort()
        for i in range(len(basket)-1,-1,-1):
            giveme.append(basket[i])
            

giveme = []
flag = 0
for i in range(v):
    point = i+1
    if not point in giveme:
        visited[point] = False
        if flag:
            continue
        trace = []
        put_basket(point)
        giveme.append(point)
        
if flag:
    print(-1)
else:
    for i in range(len(giveme)-1,-1,-1):
        print(giveme[i])
# 1 2
# 2 3
# 2 4
# 3 4
# 3 6
# 4 5
# 4 6
# 5 6