def solution(friends, gifts):
    answer = 0
    dic = dict()
    for i in friends:
        if not i in dic:
            dic[i] = len(dic)
    
    lst = []
    for st in gifts:
        a,b = st.split()
        lst.append((dic[a],dic[b]))
    
    n = len(dic)
    graph = [[0]*n for _ in range(n)]
    give = [0]*n
    for i,j in lst:
        graph[i][j] += 1
        give[i] += 1
        give[j] -= 1
        
    res = [0]*n
    for i in range(n-1):
        for j in range(i+1,n):
            if graph[i][j] > graph[j][i]:
                res[i] += 1
                
            elif graph[i][j] < graph[j][i]:
                res[j] += 1
            
            elif give[i] > give[j]:
                res[i] += 1
            
            elif give[i] < give[j]:
                res[j] += 1
    
    for i in graph:
        print(*i)
    print(give)
    print(res)
    return max(res)