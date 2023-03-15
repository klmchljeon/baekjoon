alp = [chr(i+ord('A')) for i in range(26)]
dic = dict(zip(alp,range(1,27)))
lend = 26

def solution(msg):
    global lend
    answer = []
    n = len(msg)
    idx = 0
    st = ''
    prev = ''
    while True:
        st += msg[idx]
        if not st in dic:
            lend += 1
            dic[st] = lend
            answer.append(dic[prev])
            st = ''
        
        else:
            idx += 1
        
        if idx == n:
            break
            
        prev = st
    
    if not st in dic:
        dic[st] = lend + 1
        answer.append(dic[prev])
    else:
        answer.append(dic[st])
    
    return answer