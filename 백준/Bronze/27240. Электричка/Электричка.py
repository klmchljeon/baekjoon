n,a,b = map(int,input().split())
s,t = map(int,input().split())
if s > t: s,t = t,s

if t <= a or b <= s:
    print('Outside')

elif a < s and t < b:
    print('City')

else:
    print('Full')