import sys
input = sys.stdin.readline
n=int(input())
d=list(map(int,input().split()))
print(max(d)*min(d))