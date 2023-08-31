import sys
input = sys.stdin.readline

n = int(input())
k = 1
for i in range(20000):
    print(f'? {k}')
    sys.stdout.flush()
    t = input().rstrip()
    if t == 'Y':
        print(f'! {k}')
        break