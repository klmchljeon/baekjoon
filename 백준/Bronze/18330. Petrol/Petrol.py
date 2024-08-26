n = int(input())
p = int(input()) + 60

res = min(p,n)*1500 + max(0,n-p)*3000
print(res)