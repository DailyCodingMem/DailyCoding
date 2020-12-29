def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        cut_arr = array[i-1:j]
        cut_arr.sort()
        answer.append(cut_arr[k-1])
    return answer

