#공유기 설치
import sys
input = sys.stdin.readline

def check(i):
    temp = d[0]
    count = 1
    for house in d:
        if house - temp >= i:
            temp = house
            count += 1

    return count >= c

n,c = map(int,input().split())
d = []
for _ in range(n):
    t = int(input())
    d.append(t)

d.sort()

s,e = 1,1000000001
while s+1<e:
    m = (s+e)//2
    if check(m):
        s = m
    else:
        e = m

print(s)