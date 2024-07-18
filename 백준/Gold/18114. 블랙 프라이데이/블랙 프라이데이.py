def find(num,s):
    e = n
    while s+1<e:
        mid = (s+e)//2
        if num + lst[mid] <= c:
            s = mid

        else:
            e = mid

    return num + lst[s] == c

n,c = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

for i in range(n):
    if lst[i] == c:
        print(1)
        exit()

    for j in range(i+1,n):
        tmp = lst[i] + lst[j]
        if tmp == c:
            print(1)
            exit()

        if j == n-1: continue
        if find(tmp, j+1):
            print(1)
            exit()

print(0)