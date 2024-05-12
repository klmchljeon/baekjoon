n,k = map(int,input().split())
st = input()

a = ord('A')
lst = [ord(i) - a for i in st]

idx = 0
while k:
    while idx < n and lst[idx] == 0:
        idx += 1

    if idx == n:
        lst[n-1] = (lst[n-1] + k)%26
        break

    if 26 - lst[idx] <= k:
        k -= 26 - lst[idx]
        lst[idx] = 0
        continue

    idx += 1

res = [chr(i + a) for i in lst]
print(''.join(res))