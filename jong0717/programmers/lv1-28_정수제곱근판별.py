def solution(n):
    root_n = n ** (1/2)
    if root_n == int(root_n):
        return (root_n+1)**2
    
    return -1


print(121**(1/2)==int(11.0))
# 11.0과 11은 채점시에도 같은값으로 인정!
print(solution(121))