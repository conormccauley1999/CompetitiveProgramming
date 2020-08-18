t = int(input())
for _ in range(t):
    n = int(input())
    vs = []
    for _ in range(n):
        vs.append(int(input()))
    h = sum(vs) / 2
    mx = max(vs)
    i = vs.index(mx)
    if vs.count(mx) != 1:
        print("no winner")
        continue
    elif mx > h:
        print(f"majority winner {i + 1}")
    else:
        print(f"minority winner {i + 1}")
