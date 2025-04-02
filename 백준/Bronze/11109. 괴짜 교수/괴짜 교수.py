t = int(input())
for case in range(t):
    d,n,s,p_ = map(int,input().split())
    p = d+p_*n
    q = s*n
    if p == q:
        print('does not matter')
    elif p > q:
        print('do not parallelize')
    else:
        print('parallelize')