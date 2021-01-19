import sys
sys.stdin = open("1991in.txt",'r')

import sys
def whois_mother(a):
    global ba
    for i in range(65,65+n):
        if ba[chr(i)][0] == a or ba[chr(i)][1] == a:
            return whois_mother(chr(i))
    return a

def junwe(a):
    global ba,resJeon
    resJeon.append(a)
    left,right = ba[a][0],ba[a][1]
    if left.isalpha():
        junwe(left)
    if right.isalpha():
        junwe(right)

def whowe(a):
    global ba,resWho
    left,right = ba[a][0],ba[a][1]
    if left.isalpha():
        whowe(left)
    resWho.append(a)
    if right.isalpha():
        whowe(right)
    
def jungwe(a):
    global ba, resjung
    left,right = ba[a][0],ba[a][1]
    if left.isalpha():
        jungwe(left)
    if right.isalpha():
        jungwe(right)
    resjung.append(a)

n = int(sys.stdin.readline())
ba = {}
for i in range(n):
    a,b,c = sys.stdin.readline().split()
    ba[a] = [b,c]
mom = whois_mother("A")
resJeon = []
resWho = []
resjung = []
junwe(mom)
whowe(mom)
jungwe(mom)
ans = ""
for i in resJeon:
    ans+=i
print(ans)
ans = ""
for i in resWho:
    ans+=i
print(ans)
ans = ""
for i in resjung:
    ans+=i
print(ans)