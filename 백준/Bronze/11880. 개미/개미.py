#개미
import sys
input = sys.stdin.readline

t = int(input())
for case in range(t):
    a,b,c = sorted(map(int,input().split()))
    print((a+b)**2 + c**2)