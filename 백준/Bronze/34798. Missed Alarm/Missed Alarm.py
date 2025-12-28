h1,m1 = map(int,input().split(':'))
t1 = h1*60 + m1

h2,m2 = map(int,input().split(':'))
t2 = h2*60 + m2

print('YES' if t1 < t2 else 'NO')