n = int(input())
r = 0
for _ in range(n):
    l = input().lower()
    if "pink" in l or "rose" in l:
        r += 1
print("I must watch Star Wars with my daughter" if r == 0 else r)
