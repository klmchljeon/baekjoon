n,k = map(int,input().split())
d = [i for i in range(1,n+1)]
ind = 0
result = []
for i in range(n,0,-1):
    ind += k-1
    while True:
        if ind<i:
            break
        else:
            ind-=i
    result.append(d[ind])
    del d[ind]
print("<",end='')
for i in range(n-1):
    print(result[i],end=', ')
print(result[-1],">",sep='')