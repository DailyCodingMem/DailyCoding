import sys
sys.stdin = open("2205in.txt",'r')

for count in range(int(input())):
    N = int(input())
    print("#{0}".format(count+1))
    for N in range(1,N+1):
        List =[1]*N # N 은 1부터 시작
        if N >= 3:
            for Pa_Num in range(1,len(List)-1):
                List[Pa_Num] = Last_List[Pa_Num-1]+Last_List[Pa_Num] # 이전 리스트에서 왼쪽 , 오른쪽 더한다.
            pass
        Last_List = List # 마지막 결과 리스트를 Last_List로 저장
        print(" ".join(map(str,List))) 