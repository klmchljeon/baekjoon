n,k = map(int,input().split())
st = input()
res = 0
for s1 in range(n-1):
    for e1 in range(s1+1,n):
        if st[s1]=='X' or st[s1] != st[e1]: continue

        res = max(res,e1-s1+1)

        for s2 in range(e1+1,n-1):
            for e2 in range(s2+1,n):
                if st[s2]=='X' or st[s2] != st[e2]: continue

                res = max(res,(e1-s1+1) + (e2-s2+1))

print(n-res)