def solution(scoville, K):
    answer = 0
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
q = []
for i in range(len(scoville)-1):
    if scoville[i] < K:
        q.append(scoville[i] + scoville[i+1])
    
