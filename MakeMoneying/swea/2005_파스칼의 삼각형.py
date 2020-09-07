import sys
sys.stdin = open("2205in.txt",'r')

T = int(input())
for count in range(T):
    N = int(input())
    print("#{0}".format(count+1))
    for N in range(1,N+1):
        List =[1]*N
        if N >= 3:
            for Pa_Num in range(1,len(List)-1):
                List[Pa_Num] = Last_List[Pa_Num-1]+Last_List[Pa_Num] 
            pass
        Last_List = List
        print(" ".join(map(str,List)))
        