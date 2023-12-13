n = int(input())
res = [0,1001]
for _ in range(n):
    x,y = map(int,input().split())
    if res[1] > y:
        res = [x,y]

print(*res)