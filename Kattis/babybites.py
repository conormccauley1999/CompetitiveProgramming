_ = input()
ns = input().split()
t = 1
v = True
for n in ns:
    if n != 'mumble':
        x = int(n)
        if x != t:
            v = False
            break
    t += 1
if v:
    print('makes sense')
else:
    print('something is fishy')
