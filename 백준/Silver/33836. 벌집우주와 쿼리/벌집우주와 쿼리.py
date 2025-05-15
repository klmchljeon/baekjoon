import sys
input = sys.stdin.readline

t = int(input())
for case in range(t):
    x,y = map(int,input().split())
    if y == 0 and x >= 0:
        print(0)
        continue

    if x == y or x*y == 0:
        print(1)
        continue

    if y < 0 and x > y:
        print(1)
        continue

    if y > 0 and x > 0:
        print(1)
        continue

    print(2)
