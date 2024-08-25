n,m = map(int,input().split())
lst = [[None,None] for _ in range(n+1)]
for _ in range(m):
    a,b,c = input().split()
    a,c = map(int,(a,c))
    lst[a][b!='P'] = c
    
cnt1,cnt2 = 0,0
for p,m in lst[1:]:
    if p==1 and m==0:
        cnt1 += 1
    
    if p==0 or m==1:
        cnt2 += 1

print(cnt1,n-cnt2)