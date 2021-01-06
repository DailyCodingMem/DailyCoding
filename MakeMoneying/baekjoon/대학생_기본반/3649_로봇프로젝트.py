import sys
sys.stdin = open("3649in.txt",'r')

while True:
    try:
        X = int(input()) * 10000000
        N = int(input())
        List = []
        for _ in range(N):
            List.append(int(input()))
        List.sort()
        i = 0
        j = N-1
        if List:
            while True:
                result = List[i] + List[j]
                if i == j:
                    print("danger")
                    break
                if result == X:
                    print("yes {} {}".format(List[i],List[j]))
                    break
                elif result > X:
                    j -= 1
                elif result < X:
                    i += 1
        else:
            print("danger")
    except:
        break