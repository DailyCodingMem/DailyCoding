
def solution(topping):
    answer = 0
    first = {topping[0]:0}
    second = topping[:0:-1]
    print(second)
    max_len = len(set(topping))//2

    for i in range(1, len(topping)-max_len):
        new_topping = topping[i]
        first[new_topping] = 0
        second.pop()
        if len(set(first)) == len(set(second)):
            answer += 1
        

    return answer
