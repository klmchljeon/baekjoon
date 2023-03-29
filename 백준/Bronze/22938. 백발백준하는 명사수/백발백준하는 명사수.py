#백발백준하는 명사수
x1,y1,r1 = map(int,input().split())
x2,y2,r2 = map(int,input().split())

a = (x1-x2)**2 + (y1-y2)**2
b = (r1+r2)**2
print('YES' if a < b else 'NO')