import heapq
def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while scoville[0] < K :
        if len(scoville) > 1:
            heapq.heappush(scoville,heapq.heappop(scoville) + (heapq.heappop(scoville)*2))
            cnt += 1
        else:
            return -1
    return cnt

