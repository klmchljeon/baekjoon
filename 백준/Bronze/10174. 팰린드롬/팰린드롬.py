n = int(input())
for case in range(n):
    st = input().lower()
    print('Yes' if st==st[::-1] else 'No')