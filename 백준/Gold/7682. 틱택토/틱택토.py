p='XXX'
q='OOO'
d=[(0,1),(3,1),(6,1),(0,3),(1,3),(2,3),(0,4),(2,2)]
while 1:
 s=input()
 if s=='end':break
 o=s.count('O');x=s.count('X');w=0;r=0;m=x-o
 for a,b in d:
  t=s[a::b][:3]
  if t in(p,q):
   if w:r&=w==t
   else:w=t;r=1
 if w:r&=(w==q)^m
 else:r|=x+o>8
 if m<0 or m>1:r=0
 print((''if r else'in')+'valid')