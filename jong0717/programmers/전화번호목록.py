def solution(phone_book):
    phone_book.sort()
    answer = True
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            answer = False
    return answer
# phone_book = ["12","123","1235","567","88"]
# phone_book = ["456","123","789"]
phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))
# answer = True
# phone_book.sort()
# for i in range(len(phone_book)):
#     for j in range(i+1,len(phone_book)):
#         if phone_book[i] in phone_book[j]:
#             answer = False
# print(phone_book[0:])
# print(answer)
# print(phone_book)