n = int(input())
for i in range(n):
    print('@'*3*n + ' '*n + '@'*n)

for i in range(3):
    for i in range(n):
        print('@'*n + ' '*n + '@'*n + ' '*n + '@'*n)

for i in range(n):
    print('@'*n + ' '*n + '@'*3*n)