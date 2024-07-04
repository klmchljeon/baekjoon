import sys
input = sys.stdin.readline

n = int(input())
prev = 0
res = 0
for i in range(n):
    a = int(input())
    
    res += max(a - prev, 0)
    prev = a

print(res)