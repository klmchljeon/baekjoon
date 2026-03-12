n = int(input())
lst = list(map(int,input().split()))
lst.sort()
if n == 2 and lst[0] == 1:
    cnt = 0
    for i in range(1,lst[1]+1):
        cnt += lst[1]%i == 0

    if cnt!=2:
        print('YES')
        print(2)
        print(*lst)
    else:
        print('NO')
else:
    print('YES')
    print(2)
    print(lst[-1],lst[-2])