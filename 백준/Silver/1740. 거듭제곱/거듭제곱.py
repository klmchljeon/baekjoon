n = int(input())
res = 0
for i in range(40):
    if n&(1<<i):
        res += 3**i

print(res)