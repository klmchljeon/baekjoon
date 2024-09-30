d = list(map(int,input().split()))
i = d.index(20)

alice = (d[i]+d[(i+1)%20]+d[(i-1)%20])/3
print("Alice" if alice > 10.5 else "Bob")