import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
cnt = 0
for i in range(n):
    cnt += lst[i] == lst[(i+n//2)%n]

print(cnt)