def solution(name, yearning, photo):
    answer = []
    n_dict = dict()
    for i in range(len(name)):
        n_dict[name[i]] = yearning[i]
    for n_list in photo:
        total = 0
        for n in n_list:
            if n in n_dict:
                total += n_dict[n]
        answer.append(total)
    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
answer = []
n_dict = dict()
for i in range(len(name)):
    n_dict[name[i]] = yearning[i]
for n_list in photo:
    total = 0
    for n in n_list:
        if n in n_dict:
            total += n_dict[n]
    answer.append(total)
