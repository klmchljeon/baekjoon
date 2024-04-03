n = 10000
tmp = set()
for i in range(1,n+1):
    a = sum(map(int,str(i))) + i
    tmp.add(a)

res = set(range(1,n+1))

res -= tmp
print(*sorted(res),sep='\n')