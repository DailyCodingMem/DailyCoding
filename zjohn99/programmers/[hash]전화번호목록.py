# programmers - hash - 전화번호목록 (2020-11-27)
# https://programmers.co.kr/learn/courses/30/lessons/42577

import sys
sys.stdin = open("programmers/[hash]전화번호목록.txt",'r')

# 정렬해서 찾는법
# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     for i in range(0, len(phone_book)) :
#         for j in range(i+1, len(phone_book)):
#             tmp = phone_book[j]
#             if phone_book[i] in tmp[0:len(phone_book[i])] :
#                 answer = False
#                 return answer
#     return answer

# def solution(phone_book):
#     for i in range(len(phone_book)) :
#         tmp = phone_book[i]
#         len_tmp = len(tmp)
#         for j in range(len(phone_book)) :
#             if tmp == phone_book[j][:len_tmp] and i != j :
#                 return False
    
#     return True

# startswith 사용하는 방법. 문자열이 특정문자로 시작하는지 여부를 알려줌
# startswith(시작하는문자, 시작지점) - 시작하면 True
def solution(phone_book) :
    for i in range(len(phone_book)) :
        tmp = phone_book[i]
        for j in range(len(phone_book)) :
            if i != j and phone_book[j].startswith(tmp) :
                return False
    
    return True
            



T = int(input())
for _ in range(T):
    phone_book = list(input().split())

    print(solution(phone_book))    

