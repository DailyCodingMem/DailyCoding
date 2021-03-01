from string import ascii_lowercase
def solution(str1, str2):
    # str1의 집합
    o_list = []
    # str2의 집합
    t_list = []
    # 대소문자 같은것으로 보기때문에 대문자로 통일
    STR1 = str1.upper()
    STR2 = str2.upper()
    # 소문자로 저장되니까 대문자로 저장
    alpha_list = list(ascii_lowercase.upper())
    # for 돌면서 알파벳인것만 두개씩 묶어서 저장
    for i in range(len(str1)-1): # FRANCE라치면 C까지만 돌면되니까 -1
        if STR1[i] in alpha_list and STR1[i+1] in alpha_list:
            # 두개씩 묶어서 저장
            o_list.append((STR1[i]+STR1[i+1]))  
    for j in range(len(str2)-1):
        if STR2[j] in alpha_list and STR2[j+1] in alpha_list:
            t_list.append((STR2[j]+STR2[j+1]).upper()) 
    # 교집합을 구하기 위해 결국 dict 투입
    o_dict = {}
    t_dict = {}
    union = 0
    intersection = {}
    # o_list와 t_list를 딕셔너리로 만들고
    for a in o_list:
        if a in o_dict:
            o_dict[a] += 1
        else:
            o_dict[a] = 1
    for b in t_list:
        if b in t_dict:
            t_dict[b] += 1
        else:
            t_dict[b] = 1
    # o_dict의 key,val를 불러와서 key값이 t_dict에 있으면 intersection(교집합)의 key 값으로 둘중 작은값을..넣어준다.
    for key,val in o_dict.items():
        if key in t_dict:
            intersection[key] = min(val,t_dict[key])
    # 교집합의 value들을 더해주면 그게 교집합의 크기
    inter = sum(intersection.values())
    union = len(o_list) + len(t_list) - inter
    if len(o_list) == 0 and len(t_list) == 0:
        J = 1
    else:
        J = inter / union
    return int(J*65536)


