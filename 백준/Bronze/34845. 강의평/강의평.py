n,x = map(int,input().split())
lst = list(map(int,input().split()))
sum_ = sum(lst)

a = n*x - sum_
b = 100 - x
k = a//b + bool(a%b)

print(max(0,k))