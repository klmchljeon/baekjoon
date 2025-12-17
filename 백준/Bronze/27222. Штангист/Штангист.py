n = int(input())
lst = list(map(int,input().split()))
res = 0
for i in range(n):
    x,y = map(int,input().split())
    res += lst[i] * max(0, y-x)

print(res)