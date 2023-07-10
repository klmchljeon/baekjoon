max_ = int(1e9)
N, M, A, B = map(int, (input().split()))

if A > B:
    temp = A
    A = B
    B = temp

dp = [max_]*(N+1)
danger = [0]*(N+1)

for _ in range(M):
    a, b = map(int, input().split())
    for i in range(b-a+1):
        danger[i+a] = 1
if danger[B] != 1:
    dp[B] = 1
if danger[A] != 1:
    dp[A] = 1

for i in range(N+1):
    if danger[i] == 1:
        continue

    if i >= B:
        if dp[i-A] != 0 and dp[i-B] != 0:
            dp[i] = min(dp[i], dp[i-A] + 1, dp[i-B] + 1)
        elif dp[i-A] != 0:
            dp[i] = min(dp[i], dp[i-A]+1)
        elif dp[i-B] != 0:
            dp[i] = min(dp[i], dp[i-B]+1)
        else:
            continue

    elif i >= A and dp[i-A] != 0:
        dp[i] = min(dp[i], dp[i-A]+1)


if dp[N] == max_:
    print(-1)
else:
    print(dp[N])