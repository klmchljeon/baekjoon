t = int(input())
for case in range(t):
    a = input()
    b = input()
    cnt = 0
    for i in range(len(a)):
        cnt += a[i]!=b[i]

    print(f'Hamming distance is {cnt}.')