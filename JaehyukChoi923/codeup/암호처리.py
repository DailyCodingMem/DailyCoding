password = input()
ans = ''
ans2 = ''
for i in range(len(password)):
    ans += (chr((ord(password[i])+2)))
    ans2 += (chr((ord(password[i]) * 7)%80+48))
print(ans)
print(ans2)