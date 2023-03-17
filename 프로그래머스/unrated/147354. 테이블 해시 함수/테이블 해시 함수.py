def solution(data, col, row_begin, row_end):
    answer = 0
    
    f = lambda x:(x[col-1],-x[0])
    data.sort(key = f)
    
    n = len(data[0])
    for i in range(row_begin-1,row_end):
        s = 0
        for j in range(n):
            s += data[i][j]%(i+1)
            
        answer ^= s
    
    return answer