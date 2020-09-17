n = int(input())
arr = list(range(1, n+1, 2))
for i in range(len(arr)-1, -1, -1):
    # print(i, arr[len(arr)-i-1])
    if i != 0:
        print(" "*(i), end='')
        print("*"*(arr[len(arr)-i-1]))
    else:
        print("*"*(arr[len(arr)-i-1]))
