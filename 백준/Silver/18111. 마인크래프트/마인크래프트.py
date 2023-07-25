#마인크래프트
import sys
input = sys.stdin.readline

def find(i,h):
    left, right = i, r

    while left < right:
        mid = left + (right-left) // 2

        if d[mid] < h:
            left = mid + 1
        else:
            right = mid

    return right

n,m,b = map(int,input().split())
d = []
for _ in range(n):
    d += list(map(int,input().split()))

r = n*m
d.sort()

s = sum(d)
b += s
time = 2*s

result = time
height = 0

block = 0
for k in range(1,257):
    block = find(block,k)

    b -= r
    if b < 0:
        break

    time += block - 2*(r-block)
    if result >= time:
        result = time
        height = k
    else:
        break
        
print(result, height)