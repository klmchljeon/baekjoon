import sys
input = sys.stdin.readline

t = int(input())
for case in range(t):
    x,w = map(int,input().split())
    cnt = 0
    while x < w:
        x *= 2
        cnt += 1
    
    print(cnt)