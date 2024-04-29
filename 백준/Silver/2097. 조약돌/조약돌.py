n = int(input())
if n<4:
    print(4)
    exit()

m = int(n**0.5)

for i,j in [(m,m),(m,m+1),(m+1,m+1)]:
    if i*j >= n:
        print(2*(i+j-2))
        break