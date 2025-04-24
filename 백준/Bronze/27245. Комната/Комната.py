w,l,h = (int(input()) for _ in range(3))
f1 = min(w,l) >= h*2
f2 = max(w,l) <= min(w,l)*2
print('good' if f1 and f2 else 'bad')