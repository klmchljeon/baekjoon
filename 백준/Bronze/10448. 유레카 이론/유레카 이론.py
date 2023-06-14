#유레카 이론
d = [0]*1001
tmp = [1]
while tmp[-1] < 1000:
    tmp.append(tmp[-1]+len(tmp)+1)

for i in tmp:
    for j in tmp:
        for k in tmp:
            if i+j+k <= 1000:
                d[i+j+k] = 1

t = int(input())
for case in range(t):
    k = int(input())
    print(d[k])