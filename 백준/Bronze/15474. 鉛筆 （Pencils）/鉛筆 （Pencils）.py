n,a,b,c,d = map(int,input().split())
a_ = n//a + bool(n%a)
c_ = n//c + bool(n%c)
print(min(a_*b,c_*d))