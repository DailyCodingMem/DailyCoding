def solution(record):
    answer = []
    uid_dict = {}
    for rec in record:
        if rec.split(' ')[0] == 'Enter' or rec.split(' ')[0] == 'Change':
            uid_dict[rec.split(' ')[1]] = rec.split(' ')[2]
    for rec in record:
        if rec.split(' ')[0] == 'Enter':
            answer.append(uid_dict[rec.split(' ')[1]] + '님이 들어왔습니다.')
        elif rec.split(' ')[0] == "Leave":
            answer.append(uid_dict[rec.split(' ')[1]] + '님이 나갔습니다.')
        else:
            pass
    return answer





