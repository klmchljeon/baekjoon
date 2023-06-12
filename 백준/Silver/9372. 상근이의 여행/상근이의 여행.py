#상근이의 여행
import sys
input = sys.stdin.readline

t = int(input())
for case in range(t):
    n,m = map(int,input().split())
    [input() for _ in range(m)]
    
    print(n-1)