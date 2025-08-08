def cal(a,b):
    return a/b * 1000

x,y = map(int,input().split())
n = int(input())
res = cal(x,y)
for _ in range(n):
    x,y = map(int,input().split())
    res = min(res,cal(x,y))

print(res)