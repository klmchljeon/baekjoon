n = int(input())
d = [int(input()) for _ in range(n)]
m = int(input())

res = 0
for i in range(m):
    num = int(input())
    res += d[num-1]

print(res)