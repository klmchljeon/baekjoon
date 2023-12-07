t = int(input())
for case in range(t):
    n = int(input())
    a,b = divmod(n,5)
    res = [*['+'*4]*a,'|'*b]
    print(*res)