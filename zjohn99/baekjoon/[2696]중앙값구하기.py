# baekjoon - [2696]중앙값구하기 (2021-01-29)
# https://www.acmicpc.net/problem/2696
import sys
from heapq import *
from copy import deepcopy
sys.stdin = open("baekjoon/[2696]중앙값구하기.txt",'r')

# https://breakcoding.tistory.com/109

T = int(input())
for t in range(1, T+1):
    M = int(input())
    N = M // 10 + 1
    mat = []
    for _ in range(N) :
        mat += list(map(int, input().split()))

    # print(mat)
    result = []
    tmp = []

    for i in range(M) :
        tmp.append(mat[i])
        heapify(tmp)
        ex_tmp = deepcopy(tmp)

        if i % 2 == 0 :
            for _ in range(len(tmp) // 2) :
                heappop(tmp)
            
            result.append(heappop(tmp))
        
        tmp = deepcopy(ex_tmp)
    print(len(result))
    for i in range(len(result)) :
        if i != 0 and i % 10 == 0 :
            print()
        print(result[i], end=" ")
    print()

# heapq.heappush(heap, item)
# 힙 불변성을 유지하면서, item 값을 heap으로 푸시합니다.

# heapq.heappop(heap)
# 힙 불변성을 유지하면서, heap에서 가장 작은 항목을 팝하고 반환합니다. 힙이 비어 있으면, IndexError가 발생합니다. 팝 하지 않고 가장 작은 항목에 액세스하려면, heap[0]을 사용하십시오.


