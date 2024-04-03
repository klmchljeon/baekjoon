#등차수열 변환
n = int(input())
lst = list(map(int,input().split()))

if n < 3:
    print(0)
    exit()

p = [(i,j) for i in (-1,0,1) for j in (-1,0,1)]

res = n+1
for x in p:
    dt = [*x]

    cnt = abs(dt[0])+abs(dt[1])
    lst[0] += dt[0]
    lst[1] += dt[1]

    d = lst[1] - lst[0]
    flag = True
    for i in range(2,n):
        t = lst[i] - lst[i-1]
        if t == d:
            dt.append(0)
        elif t+1 == d:
            cnt += 1
            dt.append(1)
        elif t-1 == d:
            cnt += 1
            dt.append(-1)
        else:
            flag = False
            break

        lst[i] += dt[i]


    for i in range(len(dt)):
        lst[i] -= dt[i]

    if flag:
        res = min(res,cnt)

print(res if res!=n+1 else -1)