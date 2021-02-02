from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    # print(*l)
    # (1, -1) (1, -1) (1, -1) (1, -1) (1, -1)
    # product(*l)
    # 각 (1,-1)에서의 경우들을 하나씩 뽑아 새롭게 원소를 만듬.
    '''예 : 각 튜플에서 1만 뽑아서 (1,1,1,1,1)
    4번까지 1뽑고 마지막만 -1뽑아서 (1,1,1,1,-1)
    위와 같은 식으로 만들수 있는 모든 경우를 뽑은 다음 sum으로 합만 
    리스트에 저장한 후 target에 해당하는 count를 세면됨.'''
    s = list(map(sum, product(*l)))
    return s.count(target)

