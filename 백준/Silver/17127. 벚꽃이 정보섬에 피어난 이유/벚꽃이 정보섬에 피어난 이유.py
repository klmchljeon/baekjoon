n = int(input())
d = list(map(int,input().split()))

ans = 0
for i in range(1,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            res = 0
            for x,y in ((0,i),(i,j),(j,k),(k,n)):
                tmp = 1
                for a in range(x,y):
                    tmp *= d[a]

                res += tmp

            ans = max(ans,res)

print(ans)