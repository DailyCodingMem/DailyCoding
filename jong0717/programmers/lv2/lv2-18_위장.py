# from itertools import combinations as comb
def solution(clothes):
    clothes_dict = {}
    # 딕셔너리로 만들어서 같은 종류의 갯수를 표시
    for cloth in clothes:
        if cloth[1] in clothes_dict:
            clothes_dict[cloth[1]] += 1
        else:
            clothes_dict[cloth[1]] = 1
    cnt = 1
    # 약수의 갯수 구하는 것과 식이 동일 
    for val in clothes_dict.values():
        cnt *= (val+1)
    # 전체(cnt)에서 옷을 안입은 경우 1을 빼줘야함
    answer = cnt -1
    return answer