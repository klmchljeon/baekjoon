m = 300
d = [0]*(m+2)
for i in range(1,m+2):
    d[i] = d[i-1] + i

w = [0]*(m+1)
for i in range(1,m+1):
    w[i] = w[i-1] + i*d[i+1]

t = int(input())
for case in range(t):
    n = int(input())
    print(w[n])