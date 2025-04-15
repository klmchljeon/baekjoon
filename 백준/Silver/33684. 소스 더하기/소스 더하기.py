n,k = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

if lst[-1] > k:
    print(0)
    exit()
    
if lst[0] <= 0:
    print(-1)
    exit()
    
res = 1
for i in range(1,n):
    res += (k-lst[i])//lst[0]
    
print(res)