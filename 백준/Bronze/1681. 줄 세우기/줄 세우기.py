n,l = input().split()
n = int(n)

res = 1
while True:
    n -= not l in str(res)
    if not n: break
    
    res += 1


print(res)