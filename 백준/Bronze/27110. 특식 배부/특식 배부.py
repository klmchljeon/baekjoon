f = lambda x:min(n,x)

n = int(input())
tmp = map(int,input().split())
a,b,c = map(f,tmp)
print(a+b+c)