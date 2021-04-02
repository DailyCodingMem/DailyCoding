#20200908
def solution(participant, completion):
    # 중복이름이 있기 때문에 dict로 value를 파악해야 해결가능
    part_dict = {}
    com_dict = {}
    # part_dict 만들기
    for name1 in participant:
        if name1 in part_dict:
            part_dict[name1] += 1
        else:
            part_dict[name1] = 1
    # com_dict 만들기
    for name2 in completion:
        if name2 in com_dict:
            com_dict[name2] += 1
        else:
            com_dict[name2] = 1
    # part_dict에서 name과 value를 가져와서
    for name, val in part_dict.items():
        # name이 com_dict에 없거나 해당 네임의 value가 
        # part_dict의 value와 다르면 통과못한것이므로
        if name not in com_dict or val != com_dict[name]:
            return name

# 시간초과...
# def solution(participant, completion):
#     for name in participant:
#         if name in completion:
#             idx = completion.index(name)
#             completion.pop(idx)
#         else:
#             return name


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

partSort = sorted(participant)
compSort = sorted(completion)
# print(partSort)
# print(compSort)
for i in range(len(partSort)):
    try:
        if partSort[i] != compSort[i]:
            print(partSort[i])
    except:
        return partSort[-1]


def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]