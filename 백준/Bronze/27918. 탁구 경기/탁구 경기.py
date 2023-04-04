#탁구 경기
import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
for i in range(1,n+1):
    cnt += input().rstrip() == 'D'
    if abs(i-2*cnt) == 2:
        print(f'{cnt}:{i-cnt}')
        exit()
    
print(f'{cnt}:{n-cnt}')