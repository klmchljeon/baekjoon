m = int(1e9)

def solution(matrix_sizes):
    n = len(matrix_sizes)
    dp = [[0]*n for _ in range(n)]
    for i in range(n-1):
        dp[i][i+1] = matrix_sizes[i][0]*matrix_sizes[i][1]*matrix_sizes[i+1][1]
        
    for size in range(2,n):
        for i in range(n-size):
            res = m
            for j in range(size):
                tmp = dp[i][i+j] + dp[i+j+1][i+size]
                tmp += matrix_sizes[i][0]*matrix_sizes[i+size][1]*matrix_sizes[i+j][1]
                
                res = min(res, tmp)
            
            dp[i][i+size] = res
            
    answer = dp[0][n-1]
    return answer