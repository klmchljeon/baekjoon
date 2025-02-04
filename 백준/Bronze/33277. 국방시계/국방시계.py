n,m = map(int,input().split())
t = 1440*m//n
a,b = divmod(t,60)
print(f'{a:02d}:{b:02d}')