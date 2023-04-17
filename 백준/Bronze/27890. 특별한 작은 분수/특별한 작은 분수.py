#특별한 작은 분수
x,n = map(int,input().split())
for i in range(n):
    if x&1:
        x = (2*x)^6
    else:
        x = (x//2)^6

print(x)