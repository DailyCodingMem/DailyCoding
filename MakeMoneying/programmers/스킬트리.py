def solution(skill, skill_trees):
    answer = 0
    for i in range(len(skill_trees)):
        learned = skill_trees[i]
        order = 0
        pre_order = True
        for book in skill:
            if book in learned:
                where = learned.index(book)
                if where >= order and pre_order:
                    order = where
                else:
                    break
            else:
                pre_order = False
        else:
            answer += 1
    return answer

skill = "CBD"
skill_trees =["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))