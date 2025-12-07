import sys
input = sys.stdin.readline

n,q = map(int,input().split())
lst = []
for _ in range(n):
    l,r,_ = map(int,input().split())
    lst.append((l,r))

left = sorted(lst,key = lambda x:x[0])
right = sorted(lst,key = lambda x:x[1])
for _ in range(q):
    x = int(input())
    l1 = max(0,left[n-1][0] - x)
    r1 = max(0,x - right[0][1])
    print(max(l1,r1))