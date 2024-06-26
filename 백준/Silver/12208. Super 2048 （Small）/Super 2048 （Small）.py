t = int(input())
for case in range(t):
    n,dir = input().split()
    n = int(n)

    lst = [list(map(int,input().split())) for _ in range(n)]

    res = [[0]*n for _ in range(n)]

    if dir == 'up':
        for line in range(n):
            tmp = []
            for i in range(n):
                if tmp and tmp[-1][0] == lst[i][line] and tmp[-1][1]:
                    tmp.pop()
                    tmp.append((lst[i][line]*2,0))

                elif lst[i][line] != 0:
                    tmp.append((lst[i][line],1))

            idx = 0
            for i in range(len(tmp)):
                res[idx][line] = tmp[i][0]
                idx += 1

    if dir == 'down':
        for line in range(n):
            tmp = []
            for i in range(n-1,-1,-1):
                if tmp and tmp[-1][0] == lst[i][line] and tmp[-1][1]:
                    tmp.pop()
                    tmp.append((lst[i][line]*2,0))

                elif lst[i][line] != 0:
                    tmp.append((lst[i][line],1))

            idx = n-1
            for i in range(len(tmp)):
                res[idx][line] = tmp[i][0]
                idx -= 1

    if dir == 'left':
        for line in range(n):
            tmp = []
            for j in range(n):
                if tmp and tmp[-1][0] == lst[line][j] and tmp[-1][1]:
                    tmp.pop()
                    tmp.append((lst[line][j]*2,0))

                elif lst[line][j] != 0:
                    tmp.append((lst[line][j],1))

            idx = 0
            for j in range(len(tmp)):
                res[line][idx] = tmp[j][0]
                idx += 1

    if dir == 'right':
        for line in range(n):
            tmp = []
            for j in range(n-1,-1,-1):
                if tmp and tmp[-1][0] == lst[line][j] and tmp[-1][1]:
                    tmp.pop()
                    tmp.append((lst[line][j]*2,0))

                elif lst[line][j] != 0:
                    tmp.append((lst[line][j],1))

            idx = n-1
            for j in range(len(tmp)):
                res[line][idx] = tmp[j][0]
                idx -= 1

    print(f'Case #{case+1}:')
    for i in res:
        print(*i)