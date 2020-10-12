N = int(input())
numbers = list(input())
answer = []
cnt = 0
while numbers:
    num = numbers.pop()
    cnt += 1
    answer.append(num)
    if cnt == 3:
        answer.append(",")
        cnt = 0
if len(answer) % 4 ==0:
    answer.pop()

print(''.join(answer[::-1]))

