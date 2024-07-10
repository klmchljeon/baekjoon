def minus(lst,num):
    lst[0] -= num
    lst[1] -= num
    return

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

cnt1 = 0
cnt2 = 0
for _ in range(n):
    m = int(input())
    cnt1 += m//2
    cnt2 += m%2

for i in (a,b):
    minus(i,cnt1)

if a[0] > 0:
    tmp = min(a[0],cnt2)
    minus(a,tmp)
    cnt2 -= tmp

if b[1] > 0:
    tmp = min(b[1],cnt2)
    minus(b,tmp)
    cnt2 -= tmp

minus(a,cnt2)

flag1 = a[0] <= 0 <= a[1]
flag2 = b[0] <= 0 <= b[1]

res = 'Yes' if flag1 and flag2 else 'No'
print(res)