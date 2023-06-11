#신나는 함수 실행
def w(a,b,c):
    if dp[a][b][c] != None:
        return dp[a][b][c]
    
    if a<b and b<c:
        dp[a][b][c-1] = w(a,b,c-1)
        dp[a][b-1][c-1] = w(a,b-1,c-1)
        dp[a][b-1][c] = w(a,b-1,c)
        return dp[a][b][c-1] + dp[a][b-1][c-1] - dp[a][b-1][c]
    
    else:
        dp[a-1][b][c] = w(a-1,b,c)
        dp[a-1][b-1][c] = w(a-1,b-1,c)
        dp[a-1][b][c-1] = w(a-1,b,c-1)
        dp[a-1][b-1][c-1] = w(a-1,b-1,c-1)
        return dp[a-1][b][c] + dp[a-1][b-1][c] + dp[a-1][b][c-1] - dp[a-1][b-1][c-1]

dp = [[[None]*21 for _ in range(21)] for _ in range(21)]
for i in range(21):
    for j in range(21):
        dp[i][j][0] = 1

for i in range(21):
    for k in range(21):
        dp[i][0][k] = 1

for j in range(21):
    for k in range(21):
        dp[0][j][k] = 1

while True:
    a,b,c = map(int,input().split())
    if a==-1 and b==-1 and c==-1: break
    a_,b_,c_ = a,b,c

    if a<=0 or b<=0 or c<=0:
        a_,b_,c_ = 0,0,0
    elif a>20 or b>20 or c>20:
        a_,b_,c_ = 20,20,20

    print(f'w({a}, {b}, {c}) = {w(a_,b_,c_)}')