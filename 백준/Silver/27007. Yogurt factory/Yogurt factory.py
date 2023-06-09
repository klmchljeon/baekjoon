#Yogurt factory
import sys
input = sys.stdin.readline

n,s = map(int,input().split())

prev = 5000
res = 0
for _ in range(n):
    c,y = map(int,input().split())
    prev = min(prev+s, c)
    
    res += prev*y

print(res)