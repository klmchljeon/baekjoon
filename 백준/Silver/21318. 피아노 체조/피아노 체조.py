import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = []
for i in range(n-1):
    if a[i] > a[i+1]:
        b.append(1)
    else:
        b.append(0)

S = [0]
for i in range(n-1):
    S.append(S[i] + b[i])

q = int(input())
for i in range(q):
    x,y = map(int,input().split())
    print(S[y-1] - S[x-1])