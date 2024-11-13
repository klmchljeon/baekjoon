import sys
input = sys.stdin.readline

def find(num):
    s,e = 0,len(lst)
    while s+1<e:
        mid = (s+e)//2

        if lst[mid][0] <= num:
            s = mid

        else:
            e = mid

    return s

n = int(input())
lst = [[1,1]]
for i in range(2,n+2):
    a,x,y = map(int,input().split())

    p = find(x)
    q = find(y)
    res = 1 if p==q and lst[p][1]==a else 2

    if lst[-1][1] != res:
        lst.append([i,res])

    print('Yes' if res==1 else 'No')