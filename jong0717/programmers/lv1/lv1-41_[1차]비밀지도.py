def solution(n, arr1, arr2):
    answer = []
    sol = []
    for i in range(len(arr1)):
        bin_a1 = format(arr1[i],'b')
        bin_a2 = format(arr2[i],'b')
        bin_num = str(int(bin_a1) + int(bin_a2))
        if len(bin_num) < n :
            bin_num = '0'*(n-len(bin_num)) + bin_num
        answer.append(bin_num)

    for ans in answer:
        result = ''
        for sc in ans:
            if sc == '1' or sc == '2':
                result += '#'
            else:
                result += ' '
        sol.append(result)
    return sol

def solution2(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer