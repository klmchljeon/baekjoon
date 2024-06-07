#수열과 쿼리 38

import sys
input = sys.stdin.readline

m = int(input())
s = 0
b = 0
for _ in range(m):
    q = input().rstrip()

    try:
        n = int(q)
        if n==3:
            print(s)
        elif n==4:
            print(b)

    except:
        o,n = map(int,q.split())
        if o==1:
            s += n
            b = b^n
        elif o==2:
            s -= n
            b = b^n