import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    x,a,b,c,d = map(int,input().split())
    lst.append((x,a,b,c,d))

res = []
for i in range(1,5):
    lst.sort(key = lambda x:(-x[i],x[0]))
    for num,*_ in lst:
        if not num in res:
            res.append(num)
            break

print(*res)