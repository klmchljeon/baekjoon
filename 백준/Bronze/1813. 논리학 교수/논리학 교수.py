n = int(input())
d = list(map(int,input().split()))

cnt = [0]*51
for i in d:
    cnt[i] += 1
    
res = 0
for i in range(1,51):
    if cnt[i] == i:
        res = i 
        
if res:
    print(res)
elif cnt[0]:
    print(-1)
else:
    print(0)