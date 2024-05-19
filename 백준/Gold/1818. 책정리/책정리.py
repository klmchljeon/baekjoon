n = int(input())
d = list(map(int,input().split()))

lis = [d[0]]

def find(num):
    s,e = -1,len(lis)-1
    while s+1<e:
        m = (s+e)//2

        if lis[m] >= num:
            e = m

        else:
            s = m

    return e

for i in d:
    if lis[-1] < i:
        lis.append(i)
    else:
        init = find(i)
        lis[init] = i

print(n-len(lis))