n = int(input())
m = int(input())
fixed = [int(input()) for _ in range(m)] + [n+1]

fibo = [1,1]
for i in range(2,n+1):
    fibo.append(fibo[i-1] + fibo[i-2])

res = 1
prev = 0
for i in range(m+1):
    length = fixed[i] - prev
    res *= fibo[length-1]
    prev = fixed[i]

print(res)