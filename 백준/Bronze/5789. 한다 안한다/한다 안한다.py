t = int(input())
for case in range(t):
    st = input()
    n = len(st)
    res = st[n//2-1] == st[n//2]
    print('Do-it' if res else 'Do-it-Not')