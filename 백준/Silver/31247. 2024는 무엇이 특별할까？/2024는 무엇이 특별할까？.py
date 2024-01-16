import sys
input = sys.stdin.readline

t = int(input())
for case in range(t):
    n,k = map(int,input().split())

    if k == 0:
        print((n+1)//2)
        continue

    if k > 60:
        print(0)
        continue

    a = 2**k
    b = 2**(k+1)
    if n < a:
        print(0)
        continue

    print((n-a)//b + 1)