n = list(input())
n[0], n[1] = n[1], n[0]
ans = 0
ans += (int(n[0])*10)
ans += int(n[1])
ans *= 2
if ans >= 100:
    temp = 0
    temp += int(str(ans)[1])*10
    temp += int(str(ans)[2])
    ans = temp
if ans <= 50:
    say = 'GOOD'
else:
    say = 'OH MY GOD'
print(ans)
print(say)
