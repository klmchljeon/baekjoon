lst = ["diamond","iron","stone"]
dic = dict(zip(lst,range(3)))
graph = [[1,1,1],[5,1,1],[25,5,1]]

def solution(picks, minerals):
    m = len(minerals)
    p = []
    for i in range(0,m,5):
        tmp = []
        for j in range(3):
            val = 0
            for k in minerals[i:i+5]:
                val += graph[j][dic[k]]
                
            tmp.append(val)
            
        p.append(tmp)

    n = sum(picks)
    p = p[:n]
                
    last = p.pop()
    p.sort()
    
    res = int(1e9)
    for i in range(3):
        tmp = picks[:]
        v = 0
        if tmp[i]:
            tmp[i] -= 1
            v += last[i]
        else:
            continue
            
        miner = p[:]
        while miner:
            for j in range(3):
                if tmp[j]:
                    tmp[j] -= 1
                    v += miner.pop()[j]
                    break
                    
        res = min(res,v)
    
    return res