arr = list(map(int, input().split()))

result = ''

def check():
    for i in arr:
        if i<=170:
            
            return "CRASH"
    return "PASS"

print(check())