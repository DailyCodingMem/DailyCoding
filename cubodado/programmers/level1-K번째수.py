def solution(array, commands):
    x=0
    answer=[]
    for z in range(len(commands)):
        i=commands[z][0]
        j=commands[z][1]
        k=commands[z][2]
        t=array[i-1:j]
        t.sort()
        answer.append(t[k-1])
    return answer