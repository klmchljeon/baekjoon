def bt():
    if len(s) == n:
        lst.append(tuple(s))
        return 
    
    for i in range(1,2*n+1):
        if not s or s[-1] < i:
            s.append(i)
            bt()
            s.pop()

    return 

n,m,k = map(int,input().split())

lst = []
s = []
bt()

q = []
for _ in range(m):
    tmp = list(map(int,input().split()))
    tmp.sort()
    q.append(tmp)

res = 0
for p in lst:
    cnt = 0
    for query in q:
        idx = 0
        for i in range(k):
            while idx < n:
                if p[idx] == query[i]:
                    break

                idx += 1
            
            else:
                break

        else:
            cnt += 1

    res = max(res,cnt)

print(res)