def m_change(s:str):
    s = s.replace('A#','a')
    s = s.replace('C#','c')
    s = s.replace('D#','d')
    s = s.replace('F#','f')
    s = s.replace('G#','g')
    return s

def timecal(music:list):
    time1 = music[0].split(':')
    time2 = music[1].split(':')
    hour = int(time2[0]) - int(time1[0])
    minute = int(time2[1]) - int(time1[1])
    if hour == 0 :
        total = minute
    else:
        total = 60 * hour + minute
    return total

def solution(m, musicinfos):
    answer = []
    m = m_change(m)
    for idx, musicinfo in enumerate(musicinfos):
        musicinfo = m_change(musicinfo)
        musicinfo = musicinfo.split(',')
        
        time = timecal(musicinfo)
        
        # 음악길이보다 재생시간이 짧을때는 처음부터 재생시간만큼만 재생
        if len(musicinfo[3]) > time:
            melody = musicinfo[0:time]

        else:
            q, r = divmod(time,len(musicinfo[3]))
            melody = musicinfo[3] * q + musicinfo[3][0:r]
        if m in melody:
            answer.append([idx, time, musicinfo[2]])

    if len(answer) != 0 :
        answer = sorted(answer, key=lambda x:(-x[1], x[0]))
        return answer[0][2]
    return "(None)"



