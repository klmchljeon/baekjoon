#톱니바퀴
from collections import deque

def rotate(idx,dir):
    f1 = idx < 3 and st[idx][2]^st[idx+1][6]==1 and not visit[idx+1]
    f2 = idx > 0 and st[idx][6]^st[idx-1][2]==1 and not visit[idx-1]
    visit[idx] = True

    if dir == 1:
        st[idx].appendleft(st[idx].pop())
    else:
        st[idx].append(st[idx].popleft())

    if f1:
        rotate(idx+1,-dir)
    if f2:
        rotate(idx-1,-dir)

    return 

st = []
for _ in range(4):
    tmp = deque(list(map(int,input())))
    st.append(tmp)

k = int(input())
for q in range(k):
    num,d = map(int,input().split())
    visit = [False]*4
    rotate(num-1,d)

res = 0
for i in range(4):
    res += st[i][0]*2**i

print(res)