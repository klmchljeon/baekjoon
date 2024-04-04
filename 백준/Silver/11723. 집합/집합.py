#집합
import sys
input = sys.stdin.readline

m = int(input())
s = 0b0

for _ in range(m):
    q,*n = input().split()
    if n: num = int(n[0])

    if q == 'add':
        s |= 0b1<<num

    elif q == 'remove':
        s &= ~(0b1<<num)

    elif q == 'check':
        if (s & 0b1<<num):
            print(1)
        else:
            print(0)

    elif q == 'toggle':
        s ^= (0b1<<num)

    elif q == 'all':
        s = 0b111111111111111111110
    
    else:
        s = 0b0