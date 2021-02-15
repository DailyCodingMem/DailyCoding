import collections
from itertools import combinations as CB
def solution(orders, course):
    answer = []
    for c in course:
        menu = []
        for order in orders:
            comb = CB(sorted(order),c)
            menu += comb
        counter = collections.Counter(menu)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]
    return sorted(answer)

