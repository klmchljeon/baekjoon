t = int(input())
for case in range(t):
    n = int(input())
    lst = list(map(int,input().split()))

    s = sum(lst)
    if s == 0:
        print(0)
        continue

    p = []
    for i in range(1,int(s**0.5)+1):
        if s%i == 0:
            p.append(i)
            if i**2 != s:
                p.append(s//i)

    res = n-1
    for num in p:
        cnt = 0
        tmp = 0
        for i in lst:
            tmp += i
            if tmp == num:
                tmp = 0
                continue

            cnt += 1
            if tmp > num:
                break

        else:
            res = min(res,cnt)

    print(res)
