def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        # 계속 갱신해주어야 pop이 가능
        skill_list = list(skill)
        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1
    return answer

