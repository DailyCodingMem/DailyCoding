# 20200908
h, m = map(int,input().split())
# m이 30분 보다 크면 그냥 30만 빼주면됨
if m >= 30:
    m = m - 30
# m이 30분 보다 작은 경우에 h가 0~23이므로 0일때를 고려하여 분기한다.
else:
    # h가 양수일때는 1 빼고 m에 30을 더하면됨.
    if h >= 1:
        h = h - 1
        m = m + 30
    else:
        h = h + 23
        m = m + 30
# f스트링으로 출력했는데 안되서 str형태로 출력하니까 되는 마법 이것은 뭐지?
print(str(h)+" "+str(m))