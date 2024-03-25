a = list(map(int,input().split()))
b = list(map(int,input().split()))

res2 = b[0]-a[0]+1
res3 = res2-1

tmp = 0
if a[1]<b[1] or (a[1]==b[1] and a[2]<=b[2]):
    tmp += 1

res1 = res3+tmp-1
print(res1,res2,res3,sep = '\n')