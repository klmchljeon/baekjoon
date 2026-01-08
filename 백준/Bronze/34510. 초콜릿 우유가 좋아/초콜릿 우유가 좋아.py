h1,h2,h3 = map(int,input().split())
n = int(input())

res = 0
res += n * h3
if n%2 == 1:
    res += (n//2 + 1) * h2
    res += h1

else:
    res += (n//2) * h2

print(res)