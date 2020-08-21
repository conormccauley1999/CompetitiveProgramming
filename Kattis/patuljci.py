ds = []
for _ in range(9):
    ds.append(int(input()))
sm = sum(ds)
for i in range(9):
    for j in range(9):
        if i == j:
            continue
        if sm - ds[i] - ds[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                print(ds[k])
            quit()
