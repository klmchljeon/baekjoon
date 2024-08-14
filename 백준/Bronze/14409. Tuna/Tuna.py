n = int(input())
x = int(input())
res = 0
for i in range(n):
    x1,x2 = map(int,input().split())
    if abs(x1-x2) > x:
        x3 = int(input())
        res += x3
    else:
        res += max(x1,x2)

print(res)