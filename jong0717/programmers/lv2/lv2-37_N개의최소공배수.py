from math import gcd
def lcm(x,y):
    return x*y // gcd(x,y) 
def solution(arr):
    while True:
        arr.append(lcm(arr.pop(),arr.pop()))
        if len(arr) == 1:
            return arr[0]
