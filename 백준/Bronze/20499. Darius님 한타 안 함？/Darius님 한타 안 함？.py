#Darius님 한타 안 함?
k,d,a = map(int,input().split('/'))
res = k+a<d or not d
print('hasu' if res else 'gosu')