a,b = map(int,input().split())

p = a*b
q = 4840*5
print(p//q + bool(p%q))