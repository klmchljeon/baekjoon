def check(lst):
    for x in range(n):
        for y in range(n):
            nx = x + 1
            ny = y + 1
            if nx < n and abs(lst[x][y]-lst[nx][y]) != 1:
                return False
            
            if ny < n and abs(lst[x][y]-lst[x][ny]) != 1:
                return False
            
    return True

n,k = map(int,input().split())
if k < n*n//2:
    print(-1)
    exit()

if n%2==0 and k%2==1:
    print(-1)
    exit()

if n%2 == 0:
    p = (k - (n*n//2))//(n*n)
    lst = [[p]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (i+j)%2 == 1:
                lst[i][j] += 1

    k -= (p*(n**2)) + (n*n)//2
    for i in range(n):
        for j in range(n):
            if k == 0: break

            if (i+j)%2 == 0:
                lst[i][j] += 2
                k -= 2

    for i in range(n):
        for j in range(n):
            if k == 0: break

            if (i+j)%2 == 1:
                lst[i][j] += 2
                k -= 2

    assert(check(lst))
    assert(k==0)
    for i in lst:
        print(*i)

else:
    p = (k - (n*n//2))//(n*n)
    lst = [[p]*n for _ in range(n)]
    
    k -= p*(n**2)
    if k%2 == 0:
        for i in range(n):
            for j in range(n):
                if (i+j)%2 == 1:
                    lst[i][j] += 1

        k -= (n*n)//2
        for i in range(n):
            for j in range(n):
                if k == 0: break

                if (i+j)%2 == 0:
                    lst[i][j] += 2
                    k -= 2

        for i in range(n):
            for j in range(n):
                if k == 0: break

                if (i+j)%2 == 1:
                    lst[i][j] += 2
                    k -= 2

        assert(k==0)
        assert(check(lst))  
        for i in lst:
            print(*i)

    else:
        for i in range(n):
            for j in range(n):
                if (i+j)%2 == 0:
                    lst[i][j] += 1

        k -= (n*n)//2 + 1
        for i in range(n):
            for j in range(n):
                if k == 0: break

                if (i+j)%2 == 1:
                    lst[i][j] += 2
                    k -= 2

        for i in range(n):
            for j in range(n):
                if k == 0: break

                if (i+j)%2 == 0:
                    lst[i][j] += 2
                    k -= 2

        assert(check(lst))
        assert(k==0)
        for i in lst:
            print(*i)