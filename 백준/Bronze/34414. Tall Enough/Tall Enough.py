n = int(input())
res = True
for _ in range(n):
    h = int(input())
    res &= h >= 48

print(res)