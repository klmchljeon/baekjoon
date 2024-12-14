n = int(input())
cnt = 0
for _ in range(n):
    q,x = map(int,input().split())
    if q == 1:
        cnt += x
    
    else:
        if cnt >= x:
            cnt -= x

        else:
            print('Adios')
            exit()

print('See you next month')