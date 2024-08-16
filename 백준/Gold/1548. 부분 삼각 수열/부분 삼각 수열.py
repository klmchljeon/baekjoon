n = int(input())
lst = list(map(int,input().split()))
lst.sort()

res = min(n,2)
for s in range(n-2):
    for e in range(s+2,n):
        flag = True
        for i in range(s,e-1):
            for j in range(i+1,e):
                for k in range(j+1,e+1):
                    flag &= lst[i]+lst[j]>lst[k]

        if flag:
            res = max(res,e-s+1)

print(res)