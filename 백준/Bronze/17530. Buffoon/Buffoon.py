
import sys
input = sys.stdin.readline

n = int(input())
p = int(input())
for _ in range(n-1):
    q = int(input())
    if p < q:
        print('N')
        exit()

print('S')