#Divide the Cash
n,num = map(int,input().split())
d = [int(input()) for _ in range(n)]

tmp = num//sum(d)

f = lambda x:tmp*x
res = map(f,d)

print(*res,sep='\n')