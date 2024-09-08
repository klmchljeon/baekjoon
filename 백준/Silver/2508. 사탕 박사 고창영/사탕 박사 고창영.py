t = int(input())
for case in range(t):
    input()
    r,c = map(int,input().split())
    lst = [input() for _ in range(r)]

    cnt = 0
    for i in range(r):
        for j in range(c-2):
            candy = lst[i][j] + lst[i][j+1] + lst[i][j+2]
            
            cnt += candy == '>o<'

    for j in range(c):
        for i in range(r-2):
            candy = lst[i][j] + lst[i+1][j] + lst[i+2][j]
            
            cnt += candy == 'vo^'

    print(cnt)