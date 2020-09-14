from collections import defaultdict

def isLower(char):
    if ord('a') <= ord(char) <= ord('z'):
        return True
    return False

def solution(str1, str2):
    set1 = set()
    set2 = set()
    s1d = defaultdict(int)
    s2d = defaultdict(int)
    str1 = str1.lower()
    str2 = str2.lower()
    
    for i in range(len(str1)-1):
        if isLower(str1[i]) and isLower(str1[i+1]):
            set1.add(str1[i]+str1[i+1]+str(s1d[str1[i]+str1[i+1]]))
            s1d[str1[i]+str1[i+1]] += 1
    for i in range(len(str2)-1):
        if isLower(str2[i]) and isLower(str2[i+1]):
            set2.add(str2[i]+str2[i+1]+str(s2d[str2[i]+str2[i+1]]))
            s2d[str2[i]+str2[i+1]] += 1
    # print(set1)
    # print(set2)
    
    p = len(set1 & set2)
    q = len(set1 | set2)
    # print(p,q)
    if q == 0:
        answer = 65536
    else:
        answer = int((p/q)*65536)
    return answer

        