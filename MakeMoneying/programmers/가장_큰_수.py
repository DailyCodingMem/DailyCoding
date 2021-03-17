def solution(numbers): 
    numbers = list(map(str, numbers)) 
    numbers.sort(key=lambda x: x*5, reverse=True) 
    return str(int(''.join(numbers)))



numbers = [66666, 1010101010, 22222]
numbers = [6, 10, 2]
print(solution(numbers))