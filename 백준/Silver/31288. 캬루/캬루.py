t = int(input())
for case in range(t):
    n,p = input().split()
    n = int(n)
    if n==1:
        print(4,2)
        continue

    p = list(p)
    s = sum(map(int,p))
    a = s%3
    b = 3-s%3

    for i in range(n):
        if int(p[i]) > 2:
            tmp = p[i]
            p[i] = str(int(p[i])-a)
            print(''.join(p),3)
            p[i] = tmp
        else:
            tmp = p[i]
            p[i] = str(int(p[i])+b)
            print(''.join(p),3)
            p[i] = tmp