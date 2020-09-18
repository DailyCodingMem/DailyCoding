from math import floor 
def solution(str1, str2):
    result1 = {}
    result2 = {}
    for i in range(len(str1)-1):
        words = str1[i:i+2]
        result = ''
        for word in words:
            if 97<=ord(word)<=122: # 소문자 이면
                result +=  chr(ord(word)-32) # 대문자
            elif 65<=ord(word)<=90:
                result += word
        if len(result)==2:
            if not result in result1:
                result1[result] = 1
            else:
                result1[result] += 1
                
    for i in range(len(str2)-1):
        words = str2[i:i+2]
        result = ''
        for word in words:
            if 97<=ord(word)<=122: # 소문자 이면
                result +=  chr(ord(word)-32) # 대문자
            elif 65<=ord(word)<=90:
                result += word
        if len(result)==2:
            if not result in result2:
                result2[result] = 1
            else:
                result2[result] += 1
    print(result1)
    print(result2)

    gyo = {}
    hab = {}
    for r1 in result1:
        if r1 in result2: # 둘다 있으면
            Max = max(result1[r1],result2[r1])
            Min = min(result1[r1],result2[r1])
            gyo[r1] = Min
            hab[r1] = Max
        else: # result1에만 있으면
            hab[r1] = result1[r1]
    
    for r2 in result2:
        if r2 in gyo: # 이미 사용한 것이면
            pass
        else:
            hab[r2] = result2[r2]
    HAB = 0
    for i in hab:
        HAB += hab[i]
    GYO = 0
    for i in gyo:
        GYO += gyo[i]
    if HAB:
        answer = floor((GYO/HAB)*65536)
    else:
        answer = 65536
    return answer





str1 = "FRANCE"
str1 = "AB"
# str1 = "handshake"
# str1 = "E=M*C^2"
str1 = "aa1+aa2"
str1 = "aba bab"
str1 = ""

str2 = "french"
str2 = "ab_b"
# str2 = "shake hands"
# str2 = "e=m*c^2"
str2 = "AAAA12"
str2 = "ab_____b_a__ba_b"
str2 = "ab1"


print(solution(str1,str2))