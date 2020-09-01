import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
a,b = map(int, input().split())
if a%2 == 0 and b%2 == 0:
    print("ㅇㄹㅇㄹ")
elif a%2 != 0 and b%2 != 0:
    print("ㄹㄹㄹ")
elif a%2 != 0 and b%2 == 0:
    print("ㅇㄴㄹㄴㅇㄹ")
else :
    print("ㅇㄹㅇㄹ")

print("ㅇㄴㄹㅇㄴ")