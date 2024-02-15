import sys
input = sys.stdin.readline

t = int(input())
for case in range(t):
    n = int(input())
    res = 1
    while n!=1:
        res = max(res,n)
        if n%2:
            n = n*3 + 1
        else:
            n = n//2

    print(res)