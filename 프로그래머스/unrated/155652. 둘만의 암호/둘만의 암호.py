def solution(s, skip, index):
    st = set([chr(i+ord('a')) for i in range(26)])
    skip = set(skip)
    
    alp = sorted(st-skip)
    n = len(alp)
    
    dic = dict(zip(alp,range(n)))
    
    answer = ''
    for i in s:
        tmp = (dic[i] + index)%n
        answer += alp[tmp]
    
    return answer