import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())

score = [0]*(n+1)
hei = [0]*(m+1)
hei[0] = n+1
max_ = 0

lst = []
for _ in range(m):
    u,v,p = map(int,input().split())
    if p == 0:
        lst.append((u,v))

    else:
        win = u if p==1 else v
        score[win] += 1
        hei[score[win]-1] -= 1
        hei[score[win]] += 1
        if max_ < score[win]:
            max_ = score[win]

cnt = 0
l = len(lst)
for i in range(1<<l):
    d = []
    for j in range(l):
        if i&(1<<j):
            d.append(1)
        else:
            d.append(0)

    for j in range(l):
        win = lst[j][d[j]]
        score[win] += 1
        hei[score[win]-1] -= 1
        hei[score[win]] += 1
        if max_ < score[win]:
            max_ = score[win]

    if score[k] == max_ and hei[score[k]] == 1:
        cnt += 1

    for j in range(l):
        win = lst[j][d[j]]
        score[win] -= 1
        hei[score[win]+1] -= 1
        hei[score[win]] += 1
        if max_ == score[win]+1 and hei[score[win]+1] == 0:
            max_ -= 1

print(cnt)