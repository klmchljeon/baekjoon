p = int(input())
for case in range(p):
    k,n = map(int,input().split())
    d = []
    for _ in range(n//10+bool(n%10)):
        tmp = map(int,input().split())
        d.extend(tmp)

    lst = sorted(d)
    idx = 0
    for i in d:
        if lst[idx] == i:
            idx += 1

    print(k,n-idx)