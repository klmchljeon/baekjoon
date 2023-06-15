#골뱅이 찍기 - 뒤집힌 ㅋ
n = int(input())
for i in range(n):
    print('@'*5*n)

for i in range(n,2*n):
    print('@'*n)

for i in range(2*n,3*n):
    print('@'*5*n)

for i in range(3*n,5*n):
    print('@'*n)