import math

class Frac:
    def __init__(self,p,q):
        self.p = p
        self.q = q

    def __add__(self,other):
        down = self.q * other.q
        up = self.p*other.q + self.q*other.p
        return Frac(up,down).div()
    
    def __mul__(self,other):
        down = self.q*other.q
        up = self.p*other.p
        return Frac(up,down).div()
    
    def __sub__(self,other):
        tmp = Frac(-other.p,other.q)
        return (self + tmp).div()
    
    def __truediv__(self,other):
        tmp = Frac(other.q,other.p)
        return (self * tmp).div()

    def __str__(self):
        tmp = self.div()
        if tmp.q == 1:
            return f'{tmp.p}'
        else:
            return f'{tmp.p}/{tmp.q}'
        
    def div(self):
        if self.q <= 0:
            self.p = -self.p
            self.q = -self.q
            
        g = math.gcd(self.p,self.q)
        p = self.p//g
        q = self.q//g
        return Frac(p,q)

a = [0,0]
for i in range(4):
    x,y = map(int,input().split())
    a[0] += x
    a[1] += y

b = [0,0]
for i in range(4):
    x,y = map(int,input().split())
    b[0] += x
    b[1] += y

a = [Frac(a[0],4),Frac(a[1],4)]
b = [Frac(b[0],4),Frac(b[1],4)]

p = (b[1]-a[1])/(b[0]-a[0])

q = a[1] - (p*a[0])
print(p,q)