n = int(input())
w = int(input())
res = max(0, 10*n + 20*(n>=3) + 50*(n==5) - 15*(w>1000))
print(res)