n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
lst = list(map(float,input().split()))
for i in range(n):
    lst[i] = int(lst[i]*10)

res = 0
for i in range(n):
    p = a[i]*lst[i]//10-b[i]
    q = a[i]-b[i]*lst[i]//10
    res += max(p,q)

print(res)