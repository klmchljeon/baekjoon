#solved.ac
import sys
input = sys.stdin.readline

def rd(a,b):
    i = a//b
    f = a/b - i
    return i + (f*10>=5)

n = int(input())
d = [int(input()) for _ in range(n)]

if not n: 
    print(0)
    exit()

d.sort()

p = rd(n*15,100)

s = 0
for i in range(p,n-p):
    s += d[i]

res = rd(s,(n-2*p))
print(res)