n, k = map(int,input().split(' '))
c_nums = [i for i in range(1,n+1)]
answer = []
num = 0
while c_nums:
    num = ((num + k - 1)) % len(c_nums)
    answer.append(str(c_nums.pop(num)))
print(f'<{", ".join(answer)}>')
    
    