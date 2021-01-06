import sys
sys.stdin = open("5052in.txt",'r')

for Count in range(int(input())):
    N = int(input())
    List = []
    for _ in range(N):
        List.append(sys.stdin.readline().strip())
    List.sort()
    flag = 0
    print(List)
    for i in range(len(List)-1):
        try:
            if List[i] == List[i+1][:len(List[i])]:
                print("NO")
                flag = 1
                break
        except:
            pass
        if flag:
            break
    else:
        print("YES")