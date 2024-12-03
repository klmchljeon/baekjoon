inf = 1

case = 0
while True:
    n = int(input())
    if n == 0:
        break

    dic = dict()
    for i in range(n):
        st = input()
        dic[st] = len(dic)

    graph = [[inf]*n for _ in range(n)]
    m = int(input())
    for _ in range(m):
        a,c,b = input().split()
        graph[dic[a]][dic[b]] = float(c)
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = max(graph[i][j], graph[i][k]*graph[k][j])

    for i in range(n):
        if graph[i][i] > 1:
            res = 'Yes'
            break

    else:
        res = 'No'

    print(f'Case {case+1}: {res}')
    input()
    case += 1