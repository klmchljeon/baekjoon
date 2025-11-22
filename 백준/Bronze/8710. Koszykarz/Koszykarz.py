k,w,m = map(int,input().split())
tmp = w-k
print(tmp//m + bool(tmp%m))