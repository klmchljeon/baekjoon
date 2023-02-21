import math
import sys
input = sys.stdin.readline

t = int(input())
for case in range(t):
    n,k=map(int,input().split())
    dig = math.floor(math.sqrt((n-1)*2/k + 0.25)-0.5)+1

    if dig%2 == 1:
        print(-int(k*(dig**2-1)*0.5) + (n-1),"R")
    else:
        print(int(k*(dig**2)*0.5) -(n-1),"L")