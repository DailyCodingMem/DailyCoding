from math import gcd
def solution(w,h):
    answer = 0
    GCD = gcd(w,h)
    rect = GCD * (w//GCD + h//GCD - 1)
    return w*h-rect


# def solution(w,h):
#     answer = 0
#     acc = min(h/w,w/h)
#     width = max(w,h)
#     lastPosition = 0
#     for y in range(1,width+1):
#         x = (acc)*y
#         if x==int(x):
#             answer += x-lastPosition
#         else:
#             answer += int(x+1) - lastPosition
#         # answer += ceil(x)-lastPosition
#         lastPosition = int(x)

#     return w*h-answer



W = 8
W = 100000000
H = 12
H = 999999999
W,H = 8,12
W,H = 6,4
W,H = 100000000,999999999


print(solution(W,H))

99999998900000000
99999998800000002
W = 100
H = 999
