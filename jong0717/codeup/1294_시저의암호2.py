# 20200907
#알파벳리스트를 만들기 위한 라이브러리 
from string import ascii_lowercase
#암호받아서
origin = list(map(str,input()))
alpha_list = list(ascii_lowercase)
#바뀐 문자 저장할 리스트
ans = []
# 입력된 문자를 돌면서
for alp in origin:
    # 공백이면 공백을 append하고
    if alp == ' ':
        ans.append(' ')
    # alp에 해당하는 인덱스를 alpha_list에서 가져와서 반대로하는거니까
    # 밀어내는 3을 더해주고 26으로 나누어준다음 새롭게 저장    
    else:
        change_num = (alpha_list.index(alp) + 3) % 26
        # 바뀐 인덱스에 해당하는 암호문을 추가
        ans.append(alpha_list[change_num])
print(''.join(ans))