#알고리즘 수업 - 피보나치 수 1
fibo = [0,1]
for i in range(40):
    fibo.append(fibo[-1]+fibo[-2])

n = int(input())
print(fibo[n],n-2)