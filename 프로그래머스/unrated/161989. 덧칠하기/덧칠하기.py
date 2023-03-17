def solution(n, m, section):
    answer = 1
    s = section[0]
    for i in section:
        if i - s >= m:
            s = i
            answer += 1
            
    return answer