List = list(map(int,input().split()))
Answer = 0
for i in List:
    if i%2: # 홀수라면
        Answer += (i//2 +1)
    else: # 짝수 번 째에는
        Answer += (i//2)*10
    
print(Answer)