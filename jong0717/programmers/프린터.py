def solution(priorities, location):
    printer = [(p,i) for i,p in enumerate(priorities)]
    q = []
    while printer:
        J = printer.pop(0)
        pri = J[0]
        p_list = [pri for pri,i in printer]
        if p_list:
            max_p = max(p_list)
        if pri >= max_p:
            q.append(J)
        else:
            printer.append(J)
    for i,pt in enumerate(q):
        if pt[1] == location:
            return i + 1


