import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for _ in range(n):
    st = input().rstrip()
    cnt += st == st[::-1]

print(cnt*(cnt-1))