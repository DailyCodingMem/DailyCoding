def solution(number, k):
    num = list(number) 
    s = len(num)
    ans = []
    for i in range(len(num)): 
        ans.append(int(num[i])) 
        if len(ans) < 2: 
            continue
        else:
            while k > 0 and ans[-2] < ans[-1]:
                ans.pop(-2)
                k -= 1
                if len(ans) == 1:
                    break
    while k > 0:
        ans.remove(min(ans))
        k -= 1
    answer = []
    for i in ans:
        answer.append(str(i))
    return ''.join(answer)