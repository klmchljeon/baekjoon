sieve = [True] * 246913
sieve[0]=False;sieve[1]=False
for i in range(2,498):
    if sieve[i]:
        for j in range(i+i,246913,i):
            sieve[j]=False
while True:
    n=int(input())
    if n==0:
        break
    count = 0
    for i in range(n+1,2*n+1):
        if sieve[i]:
            count+=1
    print(count)