t = int(input())
for case in range(t):
    n,c,st = input().split()
    n,c = map(int,(n,c))
    for i in range(c):
        st = st[n:] + st

    print(st)