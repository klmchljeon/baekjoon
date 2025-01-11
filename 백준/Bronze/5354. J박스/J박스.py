t = int(input())
for case in range(t):
    n = int(input())
    print('#'*n)
    if n == 1: 
        print()
        continue
    for _ in range(n-2):
        print('#' + 'J'*(n-2) + '#')
    print('#'*n)
    print()