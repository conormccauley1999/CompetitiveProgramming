n = int(input())
vs = []
for _ in range(n):
    vs.append(int(input()))
if len(vs) == max(vs):
    print("good job")
else:
    for i in range(1, max(vs) + 1):
        if i not in vs:
            print(i)
