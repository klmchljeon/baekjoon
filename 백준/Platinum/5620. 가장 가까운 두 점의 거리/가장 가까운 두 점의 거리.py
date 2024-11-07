import sys
input = sys.stdin.readline
inf = int(1e18)

def closest(arr):
    l = len(arr)
    if l <= 3:
        res = inf
        for i in range(l-1):
            for j in range(i+1,l):
                res = min(res,dist(arr[i],arr[j]))

        return res

    mid = l//2
    left = arr[:mid]
    right = arr[mid:]

    d = min(closest(left),closest(right))

    tmp = cal(left,right[0][0],d) + cal(right,left[-1][0],d)
    tmp.sort(key = lambda x:x[1])

    for i in range(len(tmp)-1):
        for j in range(i+1,len(tmp)):
            if (tmp[i][1]-tmp[j][1])**2 >= d:
                break

            d = min(d,dist(tmp[i],tmp[j]))

    return d

def cal(lst,x,d):
    tmp = []
    for i in lst:
        if abs(i[0]-x) <= d:
            tmp.append(i)

    return tmp

def dist(a,b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

n = int(input())
lst = []
for _ in range(n):
    x,y = map(int,input().split())
    lst.append((x,y))

lst.sort(key = lambda x:x[0])
print(closest(lst))