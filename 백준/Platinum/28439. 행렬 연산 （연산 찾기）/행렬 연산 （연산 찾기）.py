import sys
input = sys.stdin.readline

f = lambda x:-x[1]

n,m = map(int,input().split())
d = []
tmp = list(map(int,input().split()))
dif = [0]*(m-1)
for j in range(m-1):
    dif[j] = tmp[j+1] - tmp[j]
d.append(tmp)

flag = False
for i in range(n-1):
    tmp = list(map(int,input().split()))
    for j in range(m-1):
        if dif[j] != tmp[j+1] - tmp[j]:
            flag = True

    d.append(tmp)

if flag:
    print(-1)
    exit()

row = [0,0,None]
for i in range(n):
    dic = dict()
    dic[0] = 1

    for j in range(m):
        if not d[i][j] in dic:
            dic[d[i][j]] = 0

        dic[d[i][j]] += 1

    tmp = sorted(dic.items(),key = f)[0]
    
    if tmp[1] >= row[1]:
        row[0] = tmp[0]
        row[1] = tmp[1]
        row[2] = i

cal = [0,0,None]
for j in range(m):
    dic = dict()
    dic[0] = 1

    for i in range(n):
        if not d[i][j] in dic:
            dic[d[i][j]] = 0

        dic[d[i][j]] += 1

    tmp = sorted(dic.items(),key = f)[0]
    
    if tmp[1] >= cal[1]:
        cal[0] = tmp[0]
        cal[1] = tmp[1]
        cal[2] = j

r1 = [0]*(n)
c1 = [0]*(m)
idx,val = row[2],row[0]
r1[idx] = val
for j in range(m):
    c1[j] = d[idx][j] - val

idx,val = 0,c1[0]
for i in range(n):
    r1[i] = d[i][idx] - val

r2 = [0]*(n)
c2 = [0]*(m)
idx,val = cal[2],cal[0]
c2[idx] = val
for i in range(n):
    r2[i] = d[i][idx] - val

idx,val = 0,r2[0]
for j in range(m):
    c2[j] = d[idx][j] - val

q1 = n+m - (r1.count(0)+c1.count(0))
q2 = n+m - (r2.count(0)+c2.count(0))

if q1<=q2:
    print(q1)
    for i in range(n):
        if not r1[i]: continue
        print(1,i+1,r1[i])

    for j in range(m):
        if not c1[j]: continue
        print(2,j+1,c1[j])

else:
    print(q2)
    for i in range(n):
        if not r2[i]: continue
        print(1,i+1,r2[i])

    for j in range(m):
        if not c2[j]: continue
        print(2,j+1,c2[j])