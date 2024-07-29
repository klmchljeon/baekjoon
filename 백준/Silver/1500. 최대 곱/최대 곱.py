s,k = map(int,input().split())
div,mod = divmod(s,k)

res = 1
for i in range(mod):
    res *= (div+1)

for i in range(mod,k):
    res *= div

print(res)