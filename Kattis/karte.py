s = input()
d = {'P':[],'K':[],'H':[],'T':[]}
for i in range(0, len(s), 3):
    l, n = s[i], int(s[i+1:i+3])
    d[l].append(n)
o = []
for l in d:
    if len(d[l]) != len(set(d[l])):
        print('GRESKA')
        quit()
    o.append(13 - len(d[l]))
print(*o)
