import sys
input = sys.stdin.readline

t = int(input())
for case in range(t):
    input()
    n = int(input())
    s = 0
    for i in range(n):
        s += int(input())
        
    print('NO' if s%n else 'YES')