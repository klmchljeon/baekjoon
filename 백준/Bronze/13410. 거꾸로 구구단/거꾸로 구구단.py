#거꾸로 구구단
n,k = map(int,input().split())

d = [n*i for i in range(1,k+1)]
conv = lambda x:int(str(x)[::-1])

res = sorted(map(conv,d))[k-1]
print(res)