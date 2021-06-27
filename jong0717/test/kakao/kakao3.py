def solution(n, k, cmd):
    origin = [i for i in range(n)]
    nums = [i for i in range(n)]
    answer = ''
    del_list = []
    for c in cmd:
        if len(c) >=2 :
            s, i = c.split(' ')
        else:
            s = c
        
        if s == 'D':
            k += int(i)
        elif s == 'C':
            if k == len(nums) - 1:
                del_num = nums.pop(k)
                del_list.append((k,del_num))
                k -= 1
            else:
                del_num = nums.pop(k)
                del_list.append((k,del_num))
        elif s == 'U':
            k -= int(i)
        else:
            z = del_list.pop()
            nums.insert(z[0],z[1])
            k = nums[k]

    for i in origin:
        if i in nums:
            answer += 'O'
        else:
            answer += 'X'
    return answer

n = 8
k = 2 # 선택된 행의 위치
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
origin = [i for i in range(n)]
nums = [i for i in range(n)]
answer = ''
del_list = []
for c in cmd:
    if len(c) >=2 :
        s, i = c.split(' ')
    else:
        s = c
    
    if s == 'D':
        k += int(i)
    elif s == 'C':
        if k == len(nums) - 1:
            # del_num = nums.pop(k)
            nums[k] = -nums[k]
            # del_list.append((k,del_num))
            k -= 1
        else:
            # del_num = nums.pop(k)
            # del_list.append((k,del_num))
            nums[k] = -nums[k]
    elif s == 'U':
        k -= int(i)
    else:
        z = del_list.pop()
        nums.insert(z[0],z[1])
        k = nums[k]

for i in origin:
    if i in nums:
        answer += 'O'
    else:
        answer += 'X'

# print(del_list)
# print(nums)
print(answer)