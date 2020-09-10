n,k = map(int,input().split())

List = [list(0 for _ in range(n)) for _ in range(n)]
for y in range(n):
    for x in range(n):
        if y==0 or y==n-1:
            List[y][x] = '*'
        elif x == 0 or x==n-1:
            List[y][x] = '*'
        elif not (y+x+1)%k:
            List[y][x] = '*'
        else:
            List[y][x] = ' '

for y in range(n):
    for x in range(n):
        print(List[y][x],end='')
    print()

# **********
# **  *  * *
# *  *  *  *
# * *  *  **
# **  *  * *
# *  *  *  *
# * *  *  **
# **  *  * *
# *  *  *  *
# **********