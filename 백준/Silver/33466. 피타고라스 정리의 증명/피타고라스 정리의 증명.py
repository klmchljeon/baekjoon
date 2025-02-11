import sys
input = sys.stdin.readline

t = int(input())
for case in range(t):
    n = int(input())
    if n%2 == 0:
        print(2*n)
    else:
        print(2*n-1)