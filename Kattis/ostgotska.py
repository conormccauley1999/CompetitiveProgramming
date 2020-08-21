ws = input().split()
c = 0
for w in ws:
    if 'ae' in w:
        c += 1
if c / len(ws) >= 0.4:
    print('dae ae ju traeligt va')
else:
    print('haer talar vi rikssvenska')
