import sys
sys.stdin = open("2816in.txt",'r')

N = int(input())
List = list(input() for _ in range(N))
for i in range(len(List)):
    if List[i] == "KBS1":
        des1 = i
    elif List[i] == "KBS2":
        des2 = i
if des1 > des2:
    des2 += 1
print("1"*des1 +"4"*des1 + "1"*des2 + "4"*(des2-1))