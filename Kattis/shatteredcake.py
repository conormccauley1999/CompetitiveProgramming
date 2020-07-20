w = int(input())
n = int(input())
ds = []
for _ in range(n):
    ds.append(tuple(map(int, input().split())))
print(sum(w * l for w, l in ds) // w)
