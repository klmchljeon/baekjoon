c,k,p = map(int,input().split())

resultk = k * c*(c+1) / 2
resultp = p * c*(2*c+1)*(c+1) / 6

print(int(resultk + resultp))