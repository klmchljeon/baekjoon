fir = [1,2,3,4,5]*2000
sec = [2,1,2,3,2,4,2,5]*1250
thi = [3,3,1,1,2,2,4,4,5,5]*1000

def solution(answers):
    answer = []
    n = len(answers)
    d = [[],fir[:n],sec[:n],thi[:n]]
    
    tmp = []
    for i in range(1,4):
        cnt = 0
        for out,ans in zip(d[i],answers):
            cnt += out == ans
            
        tmp.append((i,cnt))
        
    f = lambda x:(-x[1],x[0])
    tmp.sort(key = f)
    
    m = tmp[0][1]
    for peo,score in tmp:
        if m == score:
            answer.append(peo)
    
    return answer