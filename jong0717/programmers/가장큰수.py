from itertools import permutations
def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    return str(int(''.join(numbers)))



def solution2(numbers):
    max_p = 0
    perms = list(permutations(numbers,len(numbers)))
    for perm in perms:
        answer = ''
        for i in perm:
            answer += str(i)
        if max_p < int(answer):
            max_p = int(answer)
    return max_p