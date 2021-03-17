def solution(number, k):
    answer = ''
    k = len(number)-k
    while k:
        A,B = number[:len(number)-k+1],number[len(number)-k+1:]
        Max_A = 0
        Max_idx = 0
        for i in range(len(A)):
            if int(A[i]) > Max_A:
                Max_A = int(A[i])
                Max_idx = i
            if Max_A==9:
                break
        answer += str(Max_A)
        number = A[Max_idx+1:] + B
        k -= 1
    print(answer)
    return answer

number = "4177252841"
k = 4
solution(number, k)