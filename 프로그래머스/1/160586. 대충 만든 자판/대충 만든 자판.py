def solution(keymap, targets):
    alpha = [chr(i + ord('A')) for i in range(26)]
    dic = dict(zip(alpha,range(26)))
    
    cnt = [-1]*26
    for i in range(26):
        tmp = 101
        for st in keymap:
            p = -1
            for j in range(len(st)):
                if st[j] == alpha[i]:
                    p = j+1
                    break
                    
            else:
                 continue
                    
            tmp = min(tmp,p)
            
        if tmp != 101:
            cnt[i] = tmp
        
    answer = []
    for st in targets:
        res = 0
        for i in st:
            if cnt[dic[i]] != -1:
                res += cnt[dic[i]]
                
            else:
                answer.append(-1)
                break
                
        else:
            answer.append(res)
    
    return answer