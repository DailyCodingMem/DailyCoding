def solution(s):
    num_dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
    'nine':9}
    answer = ''
    result = ''
    for i in s:
        if i.isnumeric():
            answer += i
        else:
            result += i
            if result in num_dict:
                answer += str(num_dict[result])
                result = ''
    return answer


s = "one4seveneight"
num_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,
'nine':9}
answer = ''
result = ''
for i in s:
    if i.isnumeric():
        answer += i
    else:
        result += i
        if result in num_dict:
            answer += str(num_dict[result])
            result = ''

print(result)
print(answer)
