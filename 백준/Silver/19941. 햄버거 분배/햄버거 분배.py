#햄버거 분배
from collections import deque

n,k = map(int,input().split())
st = input()

q = deque([])
d = []
for i in range(n):
    if st[i] == 'H':
        q.append(i)
    else:
        d.append(i)

cnt = 0
for i in d:
    while q and q[0]+k < i:
        q.popleft()

    if not q or q[0]-k > i: continue
    
    q.popleft()
    cnt += 1

print(cnt)