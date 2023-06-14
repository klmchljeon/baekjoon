#캥거루 세마리
a,b,c = map(int,input().split())
res = max(b-a,c-b)
print(res-1)