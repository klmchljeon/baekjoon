#AB
n,k = map(int,input().split())
if k > (n-n//2)*(n//2):
    print(-1)
    exit()

div,mod = divmod(k,n//2)

a = n-n//2
b = n//2

res = []
res.append('A'*div)
a -= div
res.append('B'*(b-mod))
if a:
    res.append('A')
    a -= 1
res.append('B'*mod)
res.append('A'*a)

print(''.join(res))