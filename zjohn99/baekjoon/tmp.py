def perm(arr, start, end) :
    global cnt
    # depth가 0부터 시작하여 k라면 k개를 모두 뽑은 것이므로 print
    if start == end :
        print(arr)
        cnt += 1
        return
    
    for idx in range(start, end) :
        arr[idx], arr[start] = arr[start], arr[idx]
        perm(arr, start+1, end)
        arr[idx], arr[start] = arr[start], arr[idx]

cnt = 0
arr = [0,1,2,3]
perm(arr,0, 4)
print(cnt)