#LCS 4
def find(num):
    s,e = -1,len(lis)-1
    while s+1<e:
        m = (s+e)//2

        if lis[m] >= num:
            e = m
        else:
            s = m

    return e

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

idx = [0]*(n+1)
for i in range(n):
    idx[a[i]] = i

d = [0]*n
for i in range(n):
    d[i] = idx[b[i]]
    
lis = [d[0]]

for i in d:
    if lis[-1] < i:
        lis.append(i)
    else:
        init = find(i)
        lis[init] = i

print(len(lis))