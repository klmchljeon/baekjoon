alpha = [chr(i + ord('a')) for i in range(26)]
dic = dict(zip(alpha,range(26)))

def solution(s):
    answer = []
    
    cnt = [-1]*26
    for i in range(len(s)):
        if cnt[dic[s[i]]] == -1:
            answer.append(-1)
        else:
            answer.append(i-cnt[dic[s[i]]])
        
        cnt[dic[s[i]]] = i
    
    return answer