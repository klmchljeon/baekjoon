#피보나치 수의 개수
d = [1,2]
while d[-1] <= 10**100:
    d.append(d[-1]+d[-2])

while True:
    t = input()
    if t == '0 0': break

    a,b = map(int,t.split())

    cnt = 0
    for i in d:
        if a<=i<=b:
            cnt += 1

    print(cnt)