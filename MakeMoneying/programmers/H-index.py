def solution(citations):
    citations.sort()
    Length = len(citations)
    answer = 0
    for i in range(len(citations)):
        how_many = citations[i]
        h = Length-(i) # i = 6, Length = 13, h = 7
        if how_many>=h:
            answer = h
            break
        # print(citations[i],how_many,h)
    return answer



citations = [5,5,5,5,5]
citations = [5,5,5,5]
citations = [3, 0, 6, 1, 5]
citations =  [0, 1, 1, 3, 3, 5, 6, 7, 11, 13, 15, 17, 19]
citations = [0,0,0,0]
print(solution(citations))