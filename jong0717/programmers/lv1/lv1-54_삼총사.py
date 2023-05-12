from itertools import combinations as comb

number = [-3, -2, -1, 0, 1, 2, 3]
def solution(number):
    answer = 0
    for n_list in comb(number,3):
        if sum(n_list) == 0:
            answer += 1
    return answer

print(solution(number))