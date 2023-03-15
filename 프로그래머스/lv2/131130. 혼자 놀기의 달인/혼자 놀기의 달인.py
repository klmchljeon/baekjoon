def bfs(s,n,d):
    v = [False]*n
    res = []
    
    stack = [s]
    while stack:
        x = stack.pop()
        
        nx = d[x]
        if not v[nx]:
            v[nx] = True
            stack.append(nx)
            res.append(nx)
            
    return res
    

def solution(cards):
    answer = 0
    group = [0]
    
    n = len(cards)
    for i in range(n):
        cards[i] -= 1
        
    visit = [False]*n
    for i in cards:
        if not visit[i]:
            tmp = bfs(i,n,cards)
            for j in tmp:
                visit[j] = True
    
            group.append(len(tmp))
                
    group.sort(reverse = True)
    answer = group[0]*group[1]
    
    return answer