s = []
lst = []
def dfs(n):
    if len(s) == n:
        lst.append(s[:])
        return 
    
    for i in range(n):
        if not i in s:
            s.append(i)
            dfs(n)
            s.pop()

    return 

def cal(num,order,d):
    cnt = 0
    for i in order:    
        if num >= d[i][0]:
            num -= d[i][1]
            cnt += 1
        else:
            break 
            
    return cnt
        
def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    dfs(n)
    
    for i in lst:
        answer = max(answer,cal(k,i,dungeons))
    
    return answer