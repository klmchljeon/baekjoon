n = int(input())
v = [0]*(n+1)
for i in range(1,n+1):
    k = int(input())
    v[k] = i

print(*v[1:],sep='\n')