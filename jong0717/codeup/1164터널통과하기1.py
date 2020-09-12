height = list(map(int,input().split()))
ans = []
for h in height:
    if h <= 170:
       ans.append(h)
if len(ans):
    print("CRASH")
else:
    print("PASS")
    