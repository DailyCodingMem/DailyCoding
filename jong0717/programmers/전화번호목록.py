def solution(phone_book):
    phone_book.sort()
    answer = True
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            answer = False
    return answer
