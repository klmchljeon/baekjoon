import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = [0] + list(map(int,input().split())) + [0]
cnt = 0
for i in range(1,n+1):
    cnt += lst[i-1]==0 and lst[i]==1

for _ in range(m):
    q,*ord = map(int,input().split())
    if q==0:
        print(cnt)
    else:
        i = ord[0]
        if lst[i] == 1: continue
        lst[i] = 1

        p = lst[i-1] + lst[i+1]
        if p == 0:
            cnt += 1
        elif p == 2:
            cnt -= 1