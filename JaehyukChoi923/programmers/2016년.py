def solution(a, b):
    day = 0
    if a == 1: pass
    if a == 2: day += 31
    if a == 3: day += 60
    if a == 4: day += 91
    if a == 5: day += 121
    if a == 6: day += 152
    if a == 7: day += 182
    if a == 8: day += 213
    if a == 9: day += 244
    if a == 10: day += 274
    if a == 11: day += 305
    if a == 12: day += 335
    day += b
    temp = 5
    arr = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    answer = arr[(temp+day)%7-1]
    return answer