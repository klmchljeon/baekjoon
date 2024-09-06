t = int(input())
for case in range(t):
    n,k = map(int,input().split())
    lst = list(map(int,input().split()))
    lst.sort()

    m = int(2e8) + 1

    s,e = 0,n-1
    while s<e:
        tmp = lst[s]+lst[e]

        m = min(m,abs(tmp-k))

        if tmp > k:
            e -= 1
        else:
            s += 1

    cnt = 0
    dic = dict()
    val = list(set((k+m,k-m)))
    for i in lst:
        for v in val:
            if v-i in dic:
                cnt += dic[v-i]

        if not i in dic:
            dic[i] = 0

        dic[i] += 1

    print(cnt)