n,k = map(int,input().split())
lst = []
for _ in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        tmp[j] ^= k^1

    lst.append(tmp)

row = []
for i in range(n):
    cnt = 0
    for j in range(n):
        cnt += lst[i][j]

    row.append(cnt)

col = []
for j in range(n):
    cnt = 0
    for i in range(n):
        cnt += lst[i][j]

    col.append(cnt)

f1 = True
while f1:
    f2 = True

    r = []
    for i in range(n):
        if row[i] == n:
            continue
        
        f2 = False
        if row[i] > n//2:
            r.append(i)

    c = []
    for j in range(n):
        if col[j] == n:
            continue

        f2 = False
        if col[j] > n//2:
            c.append(j)

    if f2:
        print(1)
        break

    f1 = r or c
    for i in r:
        for j in range(n):
            if lst[i][j] == 0:
                row[i] += 1
                col[j] += 1
                lst[i][j] = 1

    for j in c:
        for i in range(n):
            if lst[i][j] == 0:
                row[i] += 1
                col[j] += 1
                lst[i][j] = 1

else:
    print(0)