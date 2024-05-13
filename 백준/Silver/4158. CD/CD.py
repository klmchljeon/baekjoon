import sys
input = sys.stdin.readline

while True:
    n,m = map(int,input().split())
    if n==0 and m==0: break
    a = set()
    for i in range(n):
        a.add(int(input()))

    b = set()
    for i in range(m):
        b.add(int(input()))

    print(len(a&b))