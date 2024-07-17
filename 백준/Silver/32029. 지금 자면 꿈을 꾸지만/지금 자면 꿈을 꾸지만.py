n,a,b = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

sleep = [0] + lst[:-1]

res = 0
for x in range(a):
    
    #i번째 과제를 끝내고 자기.
    for i in range(n):
        cnt = 0
        time = 0
        sp = a
        for j in range(n):
            if lst[j] >= time + sp:
                time += sp 
                cnt += 1

            if i == j:
                time += x*b
                sp = a - x

        res = max(res,cnt)

    cnt = 0
    time = 0
    time += x*b
    sp = a - x
    for j in range(n):
        if lst[j] >= time + sp:
            time += sp
            cnt += 1

    res = max(res,cnt)

print(res)