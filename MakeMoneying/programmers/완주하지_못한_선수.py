def solution(participant,completion):
    participant.sort()
    completion.sort()
    completion.append('')
    answer = ''
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            answer = participant[i] 
            return answer
participant = 	["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
solution(participant,completion)