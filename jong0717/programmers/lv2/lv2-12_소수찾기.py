from itertools import permutations
def prime_check(a):
    if a <= 1:
        return False
    for i in range(2,a):
        if a % i == 0:
            return False
    return True

def solution(numbers):
    prime_set = set()
    for i in range(len(numbers),0,-1):
        for val in list(map("".join, permutations(numbers,i))):
            if prime_check(int(val)):
                prime_set.add(int(val))
    return len(prime_set)
