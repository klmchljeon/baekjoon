n = int(input())
res = 0
while n > 2**(res-1):
    res += 1

print(res)