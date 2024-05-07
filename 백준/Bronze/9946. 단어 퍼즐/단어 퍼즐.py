i = 1
while True:
    a = input()
    b = input()
    if a==b and a=='END': 
        break

    res = 'same' if sorted(a)==sorted(b) else 'different'
    print(f'Case {i}: {res}')
    i += 1