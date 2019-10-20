S = {
   '0': 0,'1': 1,'2': 2,'3': 3,
   '4': 4,'5': 5,'6': 6,'7': 7,
   '8': 8,'9': 9,'A': 10,'B': 11,
   'C': 12,'D': 13,'E': 14,'F': 15
}
V = dict(map(reversed, S.items()))
def toBase(n, b):
    a = []
    while n:
        n, x = divmod(n, b)
        a.append(V[x])
    return ''.join(reversed(a))
P = int(raw_input())
r = []
for x in range(0, P):
   i = raw_input().split(" ")
   K, b, n = int(i[0]), int(i[1]), int(i[2])
   r.append(sum(S[c] ** 2 for c in toBase(n, b)))
for i in range(0, P): print i+1, r[i]