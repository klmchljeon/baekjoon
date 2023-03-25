#수익
import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if not n: break

    num = [int(input()) for _ in range(n)]

    d = [0]*n
    d[0] = num[0]
    for i in range(1,n):
        d[i] = max(num[i], num[i]+d[i-1])

    print(max(d))