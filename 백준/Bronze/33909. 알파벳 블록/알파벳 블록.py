s,c,o,n = map(int,input().split())
s += n
c += o*2

print(min(s//3,c//6))